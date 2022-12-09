from typing import Optional
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from random import randrange
import pyodbc
import os


app = FastAPI()

server = os.environ['taskAPIdbHOST'] 
database = os.environ['taskAPIdbDATABASE']
cnxn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')
cursor = cnxn.cursor()


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

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i






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

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    my_posts.pop(index)
    return {}

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {"data": post_dict}
