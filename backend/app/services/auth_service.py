from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from random import randint

from sqlalchemy.orm import Session
from datetime import datetime, timezone, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext

import backend.app.models as models
import backend.app.schemas as schemas
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.environ["SECRET_KEY"]
EXPIRE_MINUTES = int(os.getenv("JWT_EXPIRE_MINUTES", "1440"))
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token")
bcrypt_context = CryptContext(schemes=["bcrypt"])


# check if the user exist using email or username
async def check_existing_user(db: Session, email: str, username: str = ""):
    return (
        db.query(models.UserModel)
        .filter(
            (models.UserModel.username == username) | (models.UserModel.email == email)
        )
        .first()
    )


# create token for authentication
# jwt token = {encode, secret_key, algorithm}
async def create_session_token(username: str, id: int):
    encode = {"username": username, "id": id}
    expire_time = datetime.now(timezone.utc) + timedelta(minutes=EXPIRE_MINUTES)
    encode.update({"exp": expire_time})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(db: Session, token: str = Depends(oauth2_bearer)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("username")
        id = payload.get("id")

        if username is None or id is None:
            return None
        db_user = db.query(models.UserModel).filter(models.UserModel.id == id).first()
        return db_user
    except JWTError:
        return None


# create user and save it in database
async def create_user(db: Session, user: schemas.CreateUser):
    db_user = models.UserModel(
        username=user.username,
        email=user.email,
        hashed_password=bcrypt_context.hash(user.password),
        name=user.name,
        dob=user.dob,
        gender=user.gender,
        profile_pic=user.profile_pic,
        bio=user.bio,
        location=user.location
    )
    db.add(db_user)
    db.commit()
    return db_user


# authenticate user for login
async def authenticate(db: Session, username: str, password: str):
    db_user = (
        db.query(models.UserModel).filter(models.UserModel.username == username).first()
    )
    if not db_user:
        return None
    if not bcrypt_context.verify(password, db_user.hashed_password):
        return None
    return db_user


# update password functions
async def generate_code(db: Session, email: str):
    import secrets

    code = str(secrets.randbelow(900000) + 10000)
    db_reset = db.query(models.RPModel).filter(models.RPModel.email == email).first()
    if db_reset:
        db_reset.code = code
    else:
        db_reset = models.RPModel(email=email, code=code)
        db.add(db_reset)
    db.commit()
    return code


async def verify_code(db: Session, email: str, code: str):
    db_reset = db.query(models.RPModel).filter(models.RPModel.email == email).first()
    if not db_reset:
        return False
    return db_reset.code == code


async def fake_email_send(email: str):
    print(f"code sent to {email}")


async def update_password(db: Session, user: models.UserModel, password: str):
    user.hashed_password = bcrypt_context.hash(password)
    db.commit()
