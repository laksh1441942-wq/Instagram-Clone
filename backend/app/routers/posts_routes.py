from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.database.db import get_db
import backend.app.schemas as schemas
import backend.app.services as services

router = APIRouter(
      prefix="/posts",
      tags=["Posts"]
)

#create new post
@router.post("/posts", response_model=schemas.Post)
def create_post(user_id : int, post : schemas.CreatePost, db : Session = Depends(get_db)):
      db_post = services.create_post(db, post, user_id)
      return db_post

#get user's all post
@router.get("/posts/{user_id}/posts", response_model=list[schemas.Post])
def get_user_posts(user_id : int, db : Session = Depends(get_db)):
      db_post = services.get_posts(db, user_id)
      if not db_post :
            raise HTTPException(status_code=404, detail="No posts found")
      return db_post
#get specific post of a user with post_id
@router.get("/posts/{user_id}/{post_id}", response_model=schemas.Post)
def get_user_post(user_id : int, post_id : int, db : Session = Depends(get_db)):
      db_post = services.get_post(db, user_id, post_id)
      if not db_post:
            raise HTTPException(status_code=404, detail="Post NOT found")
      return db_post
