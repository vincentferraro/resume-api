from typing import Union

from pydantic import BaseModel

class WorkHistoryBase(BaseModel):
    company_name:str
    start_date: str
    end_date: str
    role: str
    description: str

class WorkHistoryCreate(WorkHistoryBase):
    pass

class WorkHistory(WorkHistoryBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name:str
    lastname:str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    workhistory: list[WorkHistory] = []

    class Config:
        orm_mode = True