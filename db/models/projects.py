from sqlalchemy import  Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped,  mapped_column
from ..db import Base


class Project(Base):
    __tablename__="projects"

    id = Column(Integer, primary_key=True)
    name= Column(String)
    description= Column(String)
    link= Column(String)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="projects")

