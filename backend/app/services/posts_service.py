from sqlalchemy.orm import Session
import re

import backend.app.models as models
import backend.app.schemas as schemas


# get all post
def get_posts(db: Session, author_id: int):
    return (
        db.query(models.PostModel)
        .filter(models.PostModel.author_id == author_id)
        .order_by(models.PostModel.created_at.desc())
        .all()
    )


# get user's post by post_id
async def get_post_by_id(db: Session, post_id: int) -> schemas.Post:
    return (
        db.query(models.PostModel)
        .filter(models.PostModel.id == post_id)
        .first()
    )


# create post
def create_post(db: Session, post: schemas.CreatePost, author_id: int):
    db_post = models.PostModel(**post.model_dump(), author_id=author_id)
    db.add(db_post)
    db.commit()
    return db_post

#delete post
async def delete_post(db : Session, post_id : int):
    post =  await get_post_by_id(db, post_id)
    db.delete(post)
    db.commit()

#LIKE the post
async def like_post(db : Session, post_id : int, username : int):
    post = await get_post_by_id(db, post_id)
    if not post:
        return False, "invalid post_id"
    user = db.query(models.UserModel).filter(models.UserModel.username == username)
    if not user:
        return False, "invalid username"
    if user in models.PostModel.liked_by_user:
        return False, "already liked"
    models.PostModel.liked_by_user.append(user)
    models.PostModel.likes_count = len(models.PostModel.liked_by_user.append(user))

    db.commit()

#UNLIKE the post
async def unlike_post(db : Session, post_id : int, username : str):
    post = await get_post_by_id(db, post_id)
    if not post:
        return False, "invalid post_id"
    
    user = db.query(models.UserModel).filter(models.UserModel.username == username)

    if not user:
        return False, "invalid username"
    
    if user not in models.PostModel.liked_by_user:
        return False, "Havn't liked the post"
    
    models.PostModel.liked_by_user.remove(user)
    models.PostModel.likes_count = len(models.PostModel.liked_by_user.append(user))

    db.commit()

#get list of users who liked the post
async def list_of_liker(db : Session, post_id : int) -> list[schemas.User]:
    post = await get_post_by_id(db, post_id)
    if not post:
        return []
    posts = post.liked_by_user
    return posts



# create Hashtags
def create_hashtag(db: Session, post: models.PostModel):
    regex = r"#/w+"
    matches = re.findall(regex, post.content)
    for tags in matches:
        tag = tags[1:]
        hashtag = db.query(models.HTModel).filter(models.HTModel.name == tag).first()
        if not hashtag:
            hashtag = models.HTModel(name=tag)
            db.add(hashtag)
            db.flush()
        post.hashtag.append(hashtag)
        db.commit()
        db.refresh(post)
        return post


# find POSTS from hashtags
def find_post_from_hashtag(db: Session, hashtag: str):
    db_hashtag = db.query(models.HTModel).filter(models.HTModel.name == hashtag).first()
    if not db_hashtag:
        return None
    return db_hashtag.posts


# get random posts for feed
# return latest posts of all users
async def get_random_posts(
    db: Session, page: int = 1, limit: int = 10, hashtag: str = ""
):
    total_posts = db.query(models.PostModel).count()

    offset = (page - 1) * limit
    if offset >= total_posts:
        return []
    posts = (
        db.query(models.PostModel, models.UserModel.username)
        .join(models.UserModel)
        .order_by(models.PostModel.created_at.desc())
    )
    if hashtag:
        posts = (
            posts.join(models.post_hashtags)
            .join(models.HTModel)
            .filter(models.HTModel.name == hashtag)
        )
    result = []
    for post, username in posts:
        post_dict = post.__dict__
        post_dict["username"] = username
        result.append(post_dict)

    return result

