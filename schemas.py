from pydantic import BaseModel

class PostBase(BaseModel):
    title : str
    description : str

class CreatePost(PostBase):
    pass

class Post(PostBase):
    id : int
    user_id : int 

    class Config:
        from_attributes = True

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

