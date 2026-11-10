from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.database.db import get_db
import backend.app.schemas as schemas
import backend.app.services as services

router = APIRouter(prefix="/posts", tags=["Posts"])


# create new post
@router.post("/", response_model=schemas.Post)
def create_post(
    author_id: int, post: schemas.CreatePost, db: Session = Depends(get_db)
):
    db_post = services.create_post(db, post, author_id)
    return db_post


# get user's all post
@router.get("/{author_id}/posts", response_model=list[schemas.Post])
def get_user_posts(author_id: int, db: Session = Depends(get_db)):
    db_post = services.get_posts(db, author_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="No posts found")
    return db_post


# get specific post of a user with post_id
@router.get("/{post_id}", response_model=schemas.Post)
async def get_user_post(post_id: int, db: Session = Depends(get_db)):
    db_post = await services.get_post_by_id(db, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post NOT found")
    return db_post


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = await services.get_post_by_id(db, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post NOT found")
    await services.delete_post(db, post_id)


@router.get("/hashtags/{hashtag}")
async def get_hastag_posts(hashtag: str, db: Session = Depends(get_db)):
    return await services.find_post_from_hashtag(db, hashtag)
