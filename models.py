from sqlalchemy import  Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped,  mapped_column
from typing import List
from .db import Base

class User(Base):
    __tablename__="users"

    id= Column(Integer, primary_key=True)
    name= Column(String,index=True)
    lastname=Column(String)

    works: Mapped[List["WorkHistory"]] = relationship(back_populates="user")
    educations : Mapped[List["Education"]] = relationship(back_populates="user")
    skills : Mapped[List["Skill"]] = relationship(back_populates="user")

class WorkHistory(Base):
    __tablename__="work_history"

    id= Column(Integer, primary_key=True)
    company_name=Column(String)
    start_date=Column(String)
    end_date=Column(String)
    role=Column(String)
    description=Column(String)

    user_id : Mapped[int] = mapped_column(ForeignKey("users.id"))
    user : Mapped["User"] = relationship(back_populates="works")
    

class Education(Base):
    __tablename__="educations"

    id=Column(Integer,primary_key=True)
    title=Column(String)
    school=Column(String)
    year=Column(String)
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="educations")

class Skill(Base):
    __tablename__="skills"

    id=Column(Integer,primary_key=True)
    name=Column(String)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="skills")