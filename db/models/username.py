from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List


from ..db import Base

class Username(Base):
    __tablename__ = "usernames"

    id = Column(Integer, primary_key=True)

    username = Column(String)
    password = Column(String(128))


