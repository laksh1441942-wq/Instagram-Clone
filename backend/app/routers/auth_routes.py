from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from backend.app.database.db import get_db
import backend.app.schemas as schemas
import backend.app.services as services

router = APIRouter(prefix="/auth", tags=["Authentication"])


# sign up route
# create user
@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    db_user = await services.check_existing_user(
        db, username=user.username, email=user.email
    )
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="username or email already exists",
        )
    db_user = await services.create_user(db, user)
    access_token = await services.create_session_token(db_user.email, db_user.id)

    return {
        "access token": access_token,
        "token type": "bearer",
        "username": db_user.username,
    }


# login user
@router.post("/token")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    db_user = await services.authenticate(db, form_data.username, form_data.password)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Username or Password is Incorrect",
        )
    access_token = await services.create_session_token(db_user.username, db_user.id)
    return {"access_token": access_token, "token_type": "bearer"}


# Reset Password
@router.post("/sendcode")
async def reset_sent_code(email: str, db: Session = Depends(get_db)):
    db_user = await services.check_existing_user(db, email)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    code = await services.generate_code(db, email)
    await services.verify_code(db, email, code)


@router.post("/verifycode")
async def reset_verify_code(email: str, code: str, db: Session = Depends(get_db)):
    return await services.verify_code(db, email, code)


@router.post("/reset", status_code=status.HTTP_204_NO_CONTENT)
async def reset_password(email: str, password: str, db: Session = Depends(get_db)):
    db_user = services.get_user_from_email(db, email=email)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found"
        )
    await services.update_password(db, db_user, password)
