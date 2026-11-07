from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Table, Boolean
from datetime import datetime, date
from backend.app.database.db import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column

# Association Table for multiple Mapping
like_posts = Table(
    "Like_Posts",
    Base.metadata,
    Column("like_id", primary_key=True),
    Column("post_id", ForeignKey("Post_Table.id")),
    Column("user_id", ForeignKey("User_Table.id")),
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
    name : Mapped[str] = mapped_column(String)
    dob: Mapped[datetime] = mapped_column(DateTime)
    gender: Mapped[str] = mapped_column(String)
    profile_pic: Mapped[str] = mapped_column(String)  # link to pfp in database
    bio: Mapped[str] = mapped_column(String)
    location: Mapped[str] = mapped_column(String)

    # Mapping Post with Users
    posts = relationship("PostModel", back_populates="users")

    # multiple relation mapping
    post_liked = relationship(
        "PostModel", secondary=like_posts, back_populates="liked_by_user"
    )
