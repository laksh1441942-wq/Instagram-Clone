from sqlalchemy.orm import Session

import backend.app.models as models
import backend.app.schemas as schemas


#get all post
def get_posts(db : Session, user_id : int):
    return db.query(models.PostModel).filter(models.PostModel.user_id == user_id).all()

#get user's post by post_id
def get_post(db : Session, user_id : int, post_id : int):
    return db.query(models.PostModel).filter(models.PostModel.id == post_id, models.PostModel.user_id == user_id).first()

#create post
def create_post(db : Session, post : schemas.CreatePost, user_id : int):
    db_post = models.PostModel(**post.model_dump(), user_id = user_id)
    db.add(db_post)
    db.commit()
    return db_post
