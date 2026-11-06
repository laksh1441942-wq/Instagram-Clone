from sqlalchemy.orm import Mapped, mapped_column

from backend.app.database.db import Base


class RPModel(Base):

    __tablename__ = "Reset_Password"

    email: Mapped[str] = mapped_column(primary_key=True, unique=True)
    code: Mapped[str] = mapped_column()