from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Table, Boolean
from backend.app.database.db import Base
from datetime import datetime
from sqlalchemy.orm import relationship, Mapped, mapped_column

from backend.app.models.users_model import like_posts

class PostModel(Base):

    __tablename__ = "Post_Table"

    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id : Mapped[int] = mapped_column(Integer, ForeignKey("User_Table.id"))
    date : Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    title : Mapped[str] = mapped_column(String)
    description : Mapped[str] = mapped_column(String)

    #Mapping Users with Posts
    users = relationship("UserModel", back_populates="posts")

    #multiple relation mapping
    liked_by_user = relationship("UserModel", secondary=like_posts, back_populates="post_liked")
