from typing import Optional
from pydantic import BaseModel


class UsernameBase(BaseModel):
    username: str
    password: str

class Username(UsernameBase):
    id: int

    class Config:
        orm_mode: True


class UsernameUpdate(BaseModel):
    username: Optional[str]= None
    password: Optional[str] = None
