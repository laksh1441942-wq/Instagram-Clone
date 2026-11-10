from fastapi import APIRouter, Depends, HTTPException, status
from ..database.db import get_db

from sqlalchemy.orm import Session

import backend.app.services as services
import backend.app.schemas as schemas

router = APIRouter(prefix="/activity", tags=["Activity"])


@router.post("/follow/{username}", status_code=status.HTTP_204_NO_CONTENT)
async def follow(username : str, token : str, db : Session = Depends(get_db)):
    db_follower = await services.get_current_user(db, token)
    if not db_follower:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You haven't loged in")
    db_user = services.get_user_by_username(db, username)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    res = await services.follow(db, db_follower.username, username)
    if not res[0]:
        return res[1]


@router.post("/unfollow/{username}", status_code=status.HTTP_204_NO_CONTENT)
async def unfollow(username: str, token: str, db: Session = Depends(get_db)):
    db_follower = await services.get_current_user(db, token)
    if not db_follower:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="You haven't loged in"
        )
    db_user = services.get_user_by_username(db, username)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    res = await services.unfollow(db, db_follower.username, username)
    if not res[0]:
        return res[1]

@router.get("/followers", response_model=schemas.Followers)
async def get_followers(token : str, db : Session = Depends(get_db)):
    db_user = await services.get_current_user(db, token)
    if not db_user:
        raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
                )
    return await services.get_followers(db, db_user.id)


@router.get("/following", response_model=schemas.Following)
async def get_following(token: str, db: Session = Depends(get_db)):
    db_user = await services.get_current_user(db, token)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return await services.get_followings(db, db_user.id)


@router.get("/{username}", response_model=list[schemas.Activity])
def get_user_activity(
    username: str, page: int, limit: int, db: Session = Depends(get_db)
):
    db_user = services.get_user_by_username(db, username)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return services.get_activity_by_username(username, page, limit, db)
