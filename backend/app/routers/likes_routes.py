from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter
from backend.app.database.db import get_db

import backend.app.services as services
import backend.app.schemas as schemas

router = APIRouter(prefix="/likes", tags=["Likes"])


@router.post("/like")
async def like_post(post_id: int, username: str, db: Session = Depends(get_db)):
    post = await services.get_post_by_id(db, post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    user = services.get_user_by_username(db, username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    result = await services.like_post(db, post_id, username)
    if isinstance(result, tuple):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=result[1])
    return result


@router.post("/unlike")
async def unlike_post(post_id: int, username: str, db: Session = Depends(get_db)):
    post = await services.get_post_by_id(db, post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    user = services.get_user_by_username(db, username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    result = await services.unlike_post(db, post_id, username)
    if isinstance(result, tuple):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=result[1])
    return result


@router.get("/likes/{post_id}", response_model=list[schemas.UserSummary])
async def get_list_of_likers(post_id: int, db: Session = Depends(get_db)):
    post = await services.get_post_by_id(db, post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not Found"
        )
    return await services.list_of_liker(db, post_id)
