from sqlalchemy.orm import Session

import backend.app.models as models
import backend.app.schemas as schemas
from .auth_service import check_existing_user
from .users_service import get_user_by_id


def get_activity_by_username(
    username: str, page: int, limit: int, db: Session
) -> list[models.ActivityModel]:
    offset = (page - 1) * limit
    return (
        db.query(models.ActivityModel)
        .filter(models.ActivityModel.username == username)
        .order_by(models.ActivityModel.timestamp.desc())
        .offset(offset)
        .limit(limit)
        .all()
    )


async def follow(db: Session, follower: str, following: str) :
    db_follower = await check_existing_user(db, follower, "")
    db_following = await check_existing_user(db, following, "")
    if not db_follower or not db_following:
        return False, "User not found"
    db_follow = (
        db.query(models.FollowModel)
        .filter(
            models.FollowModel.follower_id == db_follower.id,
            models.FollowModel.following_id == db_following.id,
        )
        .first()
    )
    if db_follow:
        return False, "already follows"

    db_follow = models.FollowModel(
        follower_id=db_follower.id, following_id=db_following.id
    )
    db.add(db_follow)
    db_follower.following_count += 1
    db_following.follower_count += 1

    follow_activity = models.ActivityModel(
        username=following,
        follower_username=follower,
        follower_profile_image=db_follower.profile_pic,
    )
    db.add(follow_activity)
    db.commit()
    return True, "Done"


async def unfollow(db: Session, follower: str, following: str):
    db_follower = await check_existing_user(db, follower, "")
    db_following = await check_existing_user(db, following, "")
    if not db_follower or not db_following:
        return False, "User not found"
    db_follow = (
        db.query(models.FollowModel)
        .filter(
            models.FollowModel.follower_id == db_follower.id,
            models.FollowModel.following_id == db_following.id,
        )
        .first()
    )
    if not db_follow:
        return False, "Already unfollowed"

    db.delete(db_follow)
    db_follower.following_count -= 1
    db_following.follower_count -= 1

    db.commit()
    return True, "Done"


async def get_followers(db: Session, user_id: int) -> schemas.Followers:
    db_user = get_user_by_id(db, user_id)
    if not db_user:
        return schemas.Followers(followers=[])
    db_followers = (
        db.query(models.UserModel)
        .join(models.FollowModel, models.FollowModel.follower_id == models.UserModel.id)
        .filter(models.FollowModel.following_id == user_id)
        .all()
    )
    followers = [schemas.UserSchema.model_validate(user) for user in db_followers]

    return schemas.Followers(followers=followers)


async def get_followings(db: Session, user_id: int) -> schemas.Following:
    db_user = get_user_by_id(db, user_id)
    if not db_user:
        return schemas.Following(following=[])
    db_following = (
        db.query(models.UserModel)
        .join(models.FollowModel, models.FollowModel.following_id == models.UserModel.id)
        .filter(models.FollowModel.follower_id == user_id)
        .all()
    )
    following = [schemas.UserSchema.model_validate(user) for user in db_following]

    return schemas.Following(following=following)

async def check_following(db : Session, current_user : str, user : str):
    db_follower = await check_existing_user(db, current_user, "")
    db_following = await check_existing_user(db, user, "")
    if not db_following or not db_follower:
        return False
    db_follow = (
        db.query(models.FollowModel)
        .filter_by(follower_id=db_follower.id, following_id=db_following.id)
        .first()
    )
    if not db_follow:
        return False
    return True