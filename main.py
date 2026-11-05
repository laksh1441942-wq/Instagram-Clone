from fastapi import FastAPI, Depends, HTTPException
from db import SessionLocal, engine
import models, schemas, services
from db import get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind = engine)

app = FastAPI()
 
#create user
@app.post("/users", response_model=schemas.User, tags=["User Routes"])
def create_user( user : schemas.CreateUser, db : Session = Depends(get_db)):
        db_user = services.get_user_from_email(db, email = user.email)
        if db_user:
            raise HTTPException(status_code= 400, detail="Email already in use")
        db_user = services.create_user(db, user)
        return db_user

#get all users
@app.get("/users", response_model= list[schemas.User])
def get_all_users(skip : int, limit : int, db : Session = Depends(get_db)):
      db_user = services.get_all_user(db, skip, limit)
      return db_user

#get user by id
@app.get("/users/{user_id}", response_model= schemas.User)
def get_user_by_id(user_id : int, db : Session = Depends(get_db)):
      db_user = services.get_user(db, user_id)
      if not db_user:
            raise HTTPException(status_code=404, detail="User not Found")
      return db_user
      
#create new post
@app.post("/posts", response_model=schemas.Post)
def create_post(user_id : int, post : schemas.CreatePost, db : Session = Depends(get_db)):
      db_post = services.create_post(db, post, user_id)
      return db_post

#get user's all post
@app.get("/posts/{user_id}/posts", response_model=list[schemas.Post])
def get_user_posts(user_id : int, db : Session = Depends(get_db)):
      db_post = services.get_posts(db, user_id)
      if not db_post :
            raise HTTPException(status_code=404, detail="No posts found")
      return db_post
#get specific post of a user with post_id
@app.get("/posts/{user_id}/{post_id}", response_model=schemas.Post)
def get_user_post(user_id : int, post_id : int, db : Session = Depends(get_db)):
      db_post = services.get_post(db, user_id, post_id)
      if not db_post:
            raise HTTPException(status_code=404, detail="Post NOT found")
      return db_post



