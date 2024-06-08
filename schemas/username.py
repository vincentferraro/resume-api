from typing import Optional
from pydantic import BaseModel


class UsernameBase(BaseModel):
    username: str
    password: str
    token: str

class Username(UsernameBase):
    id: int

    class Config:
        orm_mode: True


