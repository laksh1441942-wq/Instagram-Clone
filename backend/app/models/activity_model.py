from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime

from ..database.db import Base

class ActivityModel(Base):

    __tablename__ = "Activity_Table"

    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    username : Mapped[str] = mapped_column(String)
    timestamp : Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    liked_post_id: Mapped[int | None] = mapped_column(Integer, nullable=True)
    liker_username: Mapped[str | None] = mapped_column(String, nullable=True)
    liked_profile_image: Mapped[str | None] = mapped_column(String, nullable=True)

    follower_username: Mapped[str | None] = mapped_column(String, nullable=True)
    follower_profile_image: Mapped[str | None] = mapped_column(String, nullable=True)