from pydantic import BaseModel
from datetime import datetime


class ActivityBase(BaseModel):
    username: str


class LikeActivity(ActivityBase):
    liked_post_id: int
    liker_username: str
    liker_profile_image: str


class FollowActivity(ActivityBase):
    follower_username: str
    following_profile_image: str


class Activity(ActivityBase):
    liked_post_id: int | None = None
    liker_username: str | None = None
    follower_username: str | None = None
    timestamp: datetime

    class Config:
        from_attributes = True
