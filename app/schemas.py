from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class PostBase(BaseModel):
    POS_TITLE: str
    POS_DESCRIPTION: Optional[str]
    POS_PUBLISHED: bool = True


class PostCreate(PostBase):
    pass


class Post(PostBase):
    POS_ID: int
    POS_CREATED_AT: datetime
    class Config:
        orm_mode = True