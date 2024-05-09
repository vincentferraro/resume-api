from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from db import Base

class User(Base):
    __tablename__="users"

    id= Column(Integer, primary_key=True)
    name= Column(String,index=True)
    lastname=Column(String)

    works=relationship("WorkHistory", back_populates="user")

class WorkHistory(Base):
    __tablename__="work_history"

    id= Column(Integer, primary_key=True)
    company_name=Column(String)
    start_date=Column(Date)
    end_date=Column(Date)
    role=Column(String)
    description=Column(String)
    user_id=Column(Integer,ForeignKey("users.id"))

    user=relationship("User",back_populates="workhistory")