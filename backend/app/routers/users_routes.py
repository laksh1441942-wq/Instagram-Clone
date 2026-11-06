from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session


from backend.app.database.db import get_db
import backend.app.schemas as schemas
import backend.app.services as services


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


#get user profile
@router.post("/profile", response_model=schemas.User)
async def get_current_user(token : str, db : Session = Depends(get_db)):
      db_user = await services.get_current_user(db, token=token)
      if not db_user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not authourized")
      return db_user

#get all users
@router.get("/users/*", response_model= list[schemas.User])
def get_all_users(skip : int = 0, limit : int = 5, db : Session = Depends(get_db)):
      db_user = services.get_all_user(db, skip, limit)
      return db_user

#get user by id
@router.get("/users/{user_id}", response_model= schemas.User)
def get_user_by_id(user_id : int, db : Session = Depends(get_db)):
      db_user = services.get_user_by_id(db, user_id)
      if not db_user:
            raise HTTPException(status_code=404, detail="User not Found")
      return db_user

@router.delete("/users/{user_id}")
def delete_user(user_id : int, db : Session = Depends(get_db)):
      db_user = services.get_user_by_id(db, user_id)
      if not db_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User NOT Found")
      services.delete_user(db, db_user)
      return db_user

#update username 
@router.put("/users/{username}", status_code=status.HTTP_204_NO_CONTENT)
async def update_username(token: str, user : schemas.UpdateUser, db : Session = Depends(get_db)):
      db_user = await services.get_current_user(db, token)
      if not db_user:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not autherized")
      db_user = await services.update_user(db, db_user, user)
