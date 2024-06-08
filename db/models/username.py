from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from ..db import Base

class Username(Base):
    __tablename__ = "usernames"

    id = Column(Integer, primary_key=True)

    username = Column(String)
    password = Column(String)
    token = Column(String)

    # user_id = Mapped[int] = mapped_column(ForeignKey("users.id"))
