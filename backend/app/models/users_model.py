from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Table, Boolean
from datetime import datetime
from backend.app.database.db import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column

# Association Table for multiple Mapping
like_posts = Table(
    "Like_Posts",
    Base.metadata,
    Column("like_id", Integer, primary_key=True, autoincrement=True),
    Column("post_id", ForeignKey("Post_Table.id")),
    Column("user_id", ForeignKey("User_Table.id")),
)

class FollowModel(Base):

    __tablename__ = "Follow_Table"

    follower_id : Mapped[int] = mapped_column(Integer, ForeignKey("User_Table.id"), primary_key=True)
    following_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("User_Table.id"), primary_key=True
    )

    follower = relationship(
        "UserModel",
        foreign_keys=[follower_id],
        back_populates="following",
    )
    following = relationship(
        "UserModel",
        foreign_keys=[following_id],
        back_populates="followers",
    )

class UserModel(Base):

    __tablename__ = "User_Table"

    # Basic Info

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, nullable=True)
    email: Mapped[str] = mapped_column(String, unique=True)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    # Profile Info
    name: Mapped[str] = mapped_column(String)
    dob: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    gender: Mapped[str | None] = mapped_column(String, nullable=True)
    profile_pic: Mapped[str | None] = mapped_column(
        String, nullable=True
    )  # link to pfp in database
    bio: Mapped[str | None] = mapped_column(String, nullable=True)
    location: Mapped[str | None] = mapped_column(String, nullable=True)

    # Mapping Post with Users
    posts = relationship("PostModel", back_populates="author")

    followers = relationship(
        "FollowModel",
        foreign_keys="FollowModel.following_id",
        back_populates="following",
    )
    following = relationship(
        "FollowModel",
        foreign_keys="FollowModel.follower_id",
        back_populates="follower",
    )

    # multiple relation mapping
    post_liked = relationship(
        "PostModel", secondary=like_posts, back_populates="liked_by_user"
    )

    follower_count : Mapped[int] = mapped_column(Integer, default=0)
    following_count : Mapped[int] = mapped_column(Integer, default=0)