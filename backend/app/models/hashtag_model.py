from backend.app.database.db import Base
from sqlalchemy import Integer, String, Table, Column, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

post_hashtags = Table(
    "Hash_Tag_Table",
    Base.metadata,
    Column("id", primary_key=True),
    Column("post_id", ForeignKey("Post_Table.id")),
    Column("hashtag_id", ForeignKey("Hash_Tag_Model.id")),
)


class HTModel(Base):

    __tablename__ = "Hash_Tag_Model"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, index=True, default=None)

    posts = relationship(
        "PostModel", secondary=post_hashtags, back_populates="hashtags"
    )
