from sqlalchemy.orm import Session

import models, schemas

#get user from the user id
def get_user(db : Session, user_id : int):
    return db.query(models.UserModel).filter(models.UserModel.id == user_id).first()

#get user from email id
def get_user_from_email(db : Session, email : str):
    return db.query(models.UserModel).filter(models.UserModel.email == email).first()

#get all user from skip to limit
def get_all_user(db : Session, skip : int = 0, limit : int = 10):
    return db.query(models.UserModel).offset(skip).limit(limit).all()

#create user
def create_user(db : Session, user : schemas.CreateUser):
    hash_password = user.password + "SHA256"
    db_user = models.UserModel(email = user.email, hash_password = hash_password)
    db.add(db_user)
    db.commit()
    return db_user

#get all post
def get_posts(db : Session, user_id : int):
    return db.query(models.PostModel).filter(models.PostModel.user_id == user_id).all()

#get user's post by post_id
def get_post(db : Session, user_id : int, post_id : int):
    return db.query(models.PostModel).filter(models.PostModel.id == post_id, models.PostModel.user_id == user_id).first()

#create post
def create_post(db : Session, post : schemas.CreatePost, user_id : int):
    db_post = models.PostModel(**post.model_dump(), user_id = user_id)
    db.add(db_post)
    db.commit()
    return db_post

#check if the user exist using email or username
async def check_existing_user(db : Session, email : str, username : str = ""):
    db_user = db.query(models.UserModel).filter(models.UserModel.username == username)
    if db_user:
        return db_user
    db_user = db.query(models.UserModel).filter(models.UserModel.email == email)
    if db_user:
        return db_user
    return None

#create token for authentication
async def create_session_token