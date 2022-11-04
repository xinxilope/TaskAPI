from typing import Optional
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from random import randrange


app = FastAPI()




class Post(BaseModel):
    tittle: str
    content: str
    published: bool = True
    rating: Optional[int] = None





my_posts = [{"titulo":"padrao","content":"padrao-conteudo","id":0}]





def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p






@app.get("/")
def root():
    return {"message": "Welcome to Home Page!"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,100000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    return{"post":post}