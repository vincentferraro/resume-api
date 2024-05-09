from typing import Union, Date

from pydantic import BaseModel

class WorkHistoryBase(BaseModel):
    company_name=str
    start_date:Date
    end_date: Date
    role: str
    description: str



class WorkHistory(WorkHistoryBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name:str
    lastname:str



class User(UserBase):
    id: int
    workhistory: list[WorkHistory] = []

    class Config:
        orm_mode = True