
from sqlalchemy import  Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped,  mapped_column
from typing import List
from .work_history import WorkHistory
from .education import Education
from .skill import Skill
from ..db import Base


class User(Base):
    __tablename__="users"

    id= Column(Integer, primary_key=True)
    name= Column(String,index=True)
    lastname=Column(String)

    works: Mapped[List["WorkHistory"]] = relationship(back_populates="user")
    educations : Mapped[List["Education"]] = relationship(back_populates="user")
    skills : Mapped[List["Skill"]] = relationship(back_populates="user")
