from pydantic import BaseModel, ConfigDict
from .users_schema import UserBase
from typing import Optional

class Profile(UserBase):

    follower_count : Optional[int] = 0
    following_count : Optional[int] = 0

    class Config :
        from_attributes = True

class UserSchema(BaseModel):
    profile_pic : Optional[str] = None
    username : str
    name : Optional[str] = None

    model_config = ConfigDict(from_attributes=True) 

class Followers(BaseModel):
    followers : Optional[list[UserSchema]] = []

class Following(BaseModel):
    following : Optional[list[UserSchema]] = []