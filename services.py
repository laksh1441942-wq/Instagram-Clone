from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
import models, schemas
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.environ["SECRET_KEY"]
EXPIRE_MINUTES = int(os.getenv("JWT_EXPIRE_MINUTES", "1440"))
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token")
bcrypt_context = CryptContext(schemes=["bcrypt"])

#get user from the user id
def get_user_by_id(db : Session, user_id : int):
    return db.query(models.UserModel).filter(models.UserModel.id == user_id).first()

#get user from email id
def get_user_from_email(db : Session, email : str):
    return db.query(models.UserModel).filter(models.UserModel.email == email).first()

#get all user from skip to limit
def get_all_user(db : Session, skip : int = 0, limit : int = 10):
    return db.query(models.UserModel).offset(skip).limit(limit).all()

#delete user by user_id
def delete_user(db : Session, user : models.UserModel):
    db.delete(user)
    db.commit()


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
async def check_existing_user(db: Session, email: str, username: str = ""):
    return db.query(models.UserModel).filter(
        (models.UserModel.username == username) |
        (models.UserModel.email == email)
    ).first()

#create token for authentication
# jwt token = {encode, secret_key, algorithm}
async def create_session_token(username : str, id : int):
    encode = {"username" : username, "id" : id}
    expire_time = datetime.now(timezone.utc) + timedelta(minutes=EXPIRE_MINUTES)
    encode.update({"exp" : expire_time})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(db : Session, token : str = Depends(oauth2_bearer)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username  = payload.get("username")
        id = payload.get("id")

        if username is None or id is None:
            return None
        db_user = db.query(models.UserModel).filter(models.UserModel.id == id).first()
        return db_user
    except JWTError:
        return None

#create user and save it in database
async def create_user(db : Session , user : schemas.CreateUser):
    db_user = models.UserModel(
        username = user.username,
        email = user.email,
        password = user.password,
        hashed_password = bcrypt_context.hash(user.password),
        is_active = True
    )
    db.add(db_user)
    db.commit()
    return db_user

#authenticate user for login
async def authenticate(db : Session, username : str, password : str):
    db_user = db.query(models.UserModel).filter(models.UserModel.username == username).first()
    if not db_user:
        return None
    if not bcrypt_context.verify(password, db_user.hashed_password):
        return None
    return db_user