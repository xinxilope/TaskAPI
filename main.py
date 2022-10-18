from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()



class Post(BaseModel):
    tittle: str
    content: str
    published: bool = True
    rating: Optional[int] = None






@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": "this is all your posts"}

@app.post("/createposts")
def create_posts(post: Post):
    print(post.dict())
    return {"data": post}