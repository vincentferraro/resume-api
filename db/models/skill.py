from sqlalchemy import  Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped,  mapped_column
from typing import List
from ..db import Base
# from user import User


class Skill(Base):
    __tablename__="skills"

    id=Column(Integer,primary_key=True)
    name=Column(String)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="skills")