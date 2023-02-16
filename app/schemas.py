from typing import Optional
from pydantic import BaseModel, EmailStr
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


class UserCreate(BaseModel):
    USU_EMAIL: EmailStr
    USU_PASSWORD: str


class UserOut(BaseModel):
    USU_ID: int
    USU_EMAIL: EmailStr
    USU_CREATED_AT: datetime
    
    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None