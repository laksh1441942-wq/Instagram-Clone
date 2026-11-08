from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

from backend.app.schemas.posts_schema import Post


class UserBase(BaseModel):
    username: str
    email: EmailStr
    name: str
    dob: Optional[datetime] = None
    gender: Optional[str] = None
    bio: Optional[str] = None
    location: Optional[str] = None
    profile_pic: Optional[str] = None


class CreateUser(UserBase):
    password: str = Field(min_length=8)


class UserSummary(UserBase):
    id: int

    class Config:
        from_attributes = True


class User(UserBase):
    id: int
    is_active: Optional[bool] = True
    created_at: datetime
    posts: list[Post] = Field(default_factory=list)

    class Config:
        from_attributes = True


Post.model_rebuild(_types_namespace={"UserSummary": UserSummary})


class UpdateUser(BaseModel):
    name: Optional[str] = None
    dob: Optional[datetime] = None
    gender: Optional[str] = None
    bio: Optional[str] = None
    location: Optional[str] = None
    profile_pic: Optional[str] = None
