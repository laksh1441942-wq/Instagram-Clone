from pydantic import BaseModel
from backend.app.schemas.posts_schema import Post


class UserBase(BaseModel):
    username : str
    email : str

class CreateUser(UserBase):
    password : str

class User(UserBase):
    id : int 
    is_active : bool
    posts : list[Post] = [] 

    class Config:
        from_attributes = True

class UpdateUser(BaseModel):
    username : str
