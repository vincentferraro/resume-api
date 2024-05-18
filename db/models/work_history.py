from sqlalchemy import  Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped,  mapped_column
from ..db import Base



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
    
