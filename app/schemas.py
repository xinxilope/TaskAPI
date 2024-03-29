from typing import Optional
from pydantic import BaseModel, EmailStr, conint
from datetime import datetime


class PostBase(BaseModel):
    POS_TITLE: str
    POS_DESCRIPTION: Optional[str]
    POS_PUBLISHED: bool = True


class PostCreate(PostBase):
    pass
    class Config:
        schema_extra = {
            "example": {
                "POS_TITLE": "Titulo do post",
                "POS_DESCRIPTION": "Descricao da tarefa",
                "POS_PUBLISHED": True
            }
        }


class UserOut(BaseModel):
    USU_ID: int
    USU_EMAIL: EmailStr
    USU_CREATED_AT: datetime
    class Config:
        orm_mode = True

class Post(PostBase):
    POS_ID: int
    POS_CREATED_AT: datetime
    POS_USU_ID: int
    Dono: UserOut
    class Config:
        orm_mode = True


# class PostOut(BaseModel):
#     POS_ID: int
#     likes: int


class UserCreate(BaseModel):
    USU_EMAIL: EmailStr
    USU_PASSWORD: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None


class Like(BaseModel):
    post_id: int
    dir: conint(ge=0, le=1)

class QueryGenerica(BaseModel):
    query: str