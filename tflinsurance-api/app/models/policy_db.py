# app/models/policy_db.py

from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class PolicyDB(Base):
    __tablename__ = "policies"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(255))
    maturity: Mapped[str] = mapped_column(String(50))
    premium: Mapped[float] = mapped_column(Float)