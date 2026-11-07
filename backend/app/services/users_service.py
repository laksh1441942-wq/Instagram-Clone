from sqlalchemy.orm import Session

import backend.app.models as models
import backend.app.schemas as schemas


# get user from the user id
def get_user_by_id(db: Session, user_id: int):
    return db.query(models.UserModel).filter(models.UserModel.id == user_id).first()


# get user from email id
def get_user_from_email(db: Session, email: str):
    return db.query(models.UserModel).filter(models.UserModel.email == email).first()


# get all user from skip to limit
def get_all_user(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.UserModel).offset(skip).limit(limit).all()


# delete user by user_id
def delete_user(db: Session, user: models.UserModel):
    db.delete(user)
    db.commit()


# update username
async def update_user(db: Session, db_user: models.UserModel, user: schemas.UpdateUser):
    db_user.name = user.name or db_user.name
    db.commit()
    db.refresh(db_user)
    return db_user
