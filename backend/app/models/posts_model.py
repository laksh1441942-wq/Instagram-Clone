from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Table, Boolean
from backend.app.database.db import Base
from datetime import datetime
from sqlalchemy.orm import relationship, Mapped, mapped_column

from backend.app.models.users_model import like_posts
from backend.app.models.hashtag_model import post_hashtags


class PostModel(Base):

    __tablename__ = "Post_Table"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("User_Table.id"))
    title: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)
    image: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    location: Mapped[str] = mapped_column(String)
    likes_count: Mapped[int] = mapped_column(Integer, default=0)

    # Mapping Users with Posts
    author = relationship("UserModel", back_populates="posts")

    # multiple relation mapping
    liked_by_user = relationship(
        "UserModel", secondary=like_posts, back_populates="post_liked"
    )

    hashtags = relationship("HTModel", secondary=post_hashtags, back_populates="posts")
