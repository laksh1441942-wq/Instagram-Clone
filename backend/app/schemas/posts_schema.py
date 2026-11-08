from __future__ import annotations
from datetime import datetime

from typing import TYPE_CHECKING
from pydantic import BaseModel

if TYPE_CHECKING:
    from backend.app.schemas.users_schema import UserSummary


class PostBase(BaseModel):
    title: str
    content: str


class CreatePost(PostBase):
    image: str
    location: str


class Post(PostBase):
    id: int
    author_id: int
    likes_count: int
    created_at: datetime
    liked_by_user: list[UserSummary]

    class Config:
        from_attributes = True
