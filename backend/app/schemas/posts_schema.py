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
