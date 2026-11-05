from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from db import SessionLocal, engine
import models, schemas, services
from db import get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind = engine)

app = FastAPI()
 
#sign up route
#create user 
@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user( user : schemas.CreateUser, db : Session = Depends(get_db)):
      db_user = await services.check_existing_user(db, user.username, user.email)
      if db_user:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail="username or email already exists")
      db_user = await services.create_user(db, user)
      access_token = await services.create_session_token(db_user.email, db_user.id)

      return {
            "access token" : access_token,
            "token type" : "bearer",
            "username" : db_user.username
      }

#login user
@app.post("/token")
async def login(form_data : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)):
      db_user = await services.authenticate(db, form_data.username, form_data.password)
      if not db_user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Username or Password is Incorrect")
      access_token = await services.create_session_token(db_user.username, db_user.id)
      return {
            "access_token" : access_token,
            "token_type" : "bearer"
      }

#get user profile
@app.post("/profile", response_model=schemas.User)
async def get_current_user(token : str, db : Session = Depends(get_db)):
      db_user = await services.get_current_user(db, token=token)
      if not db_user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not authourized")
      return db_user

#get all users
@app.get("/users/*", response_model= list[schemas.User])
def get_all_users(skip : int = 0, limit : int = 5, db : Session = Depends(get_db)):
      db_user = services.get_all_user(db, skip, limit)
      return db_user

#get user by id
@app.get("/users/{user_id}", response_model= schemas.User)
def get_user_by_id(user_id : int, db : Session = Depends(get_db)):
      db_user = services.get_user_by_id(db, user_id)
      if not db_user:
            raise HTTPException(status_code=404, detail="User not Found")
      return db_user

@app.delete("/users/{user_id}")
def delete_user(user_id : int, db : Session = Depends(get_db)):
      db_user = services.get_user_by_id(db, user_id)
      if not db_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User NOT Found")
      services.delete_user(db, db_user)
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



