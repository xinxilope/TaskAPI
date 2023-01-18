from pydantic import BaseModel



class PostBase(BaseModel):
    POS_TITLE: str
    POS_DESCRIPTION: str
    POS_PUBLISHED: bool = True


class PostCreate(PostBase):
    pass
