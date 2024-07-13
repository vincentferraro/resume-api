
from sqlalchemy import  Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped,  mapped_column
from typing import List
from ..db import Base
from .work_history import WorkHistory
from .education import Education
from .skill import Skill
from .projects import Project
from .username import Username

class User(Base):
    __tablename__="users"

    id= Column(Integer, primary_key=True)
    name= Column(String,index=True)
    lastname=Column(String)
    location=Column(String)
    email=Column(String)
    linkedin=Column(String)
    website=Column(String)
    username_id = Column(Integer,ForeignKey("usernames.id"))

    works: Mapped[List["WorkHistory"]] = relationship(back_populates="user")
    educations : Mapped[List["Education"]] = relationship(back_populates="user")
    skills : Mapped[List["Skill"]] = relationship(back_populates="user")
    projects : Mapped[List["Project"]] = relationship(back_populates="user")
