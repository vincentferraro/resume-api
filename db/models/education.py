from sqlalchemy import  Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped,  mapped_column
from ..db import Base
# from user import User


class Education(Base):
    __tablename__="educations"

    id=Column(Integer,primary_key=True)
    title=Column(String)
    school=Column(String)
    year=Column(String)
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="educations")
