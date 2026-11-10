from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.app import models, schemas
from backend.app.database.db import Base
from backend.app.services.posts_service import create_post


def test_create_post_persists_post_and_hashtags():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()

    try:
        post = create_post(
            session,
            schemas.CreatePost(
                title="A post",
                content="A post with #testing",
                image="",
                location="",
            ),
            author_id=3,
        )

        assert post.id is not None
        assert [hashtag.name for hashtag in post.hashtags] == ["testing"]
        assert session.query(models.PostModel).count() == 1
        assert session.query(models.HTModel).count() == 1
    finally:
        session.close()
        Base.metadata.drop_all(engine)
