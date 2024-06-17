from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from ..db.db import get_db

from typing import Annotated


router = APIRouter()


@router.post("/token/refresh")
def refresh_token(token: str, db: Session = Depends(get_db),):
    return {"token":token}