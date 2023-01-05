from typing import Optional
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from random import randrange
import pyodbc
import os
import time
import json


app = FastAPI()


class Post(BaseModel):
    tittle: str
    content: str
    published: bool = True


while True:
    try:
        server = os.environ['taskAPIdbHOST'] 
        database = os.environ['taskAPIdbDATABASE']
        cnxn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')
        cursor = cnxn.cursor()
        print("Database Connected!")
        break
    except Exception as error:
        print("Connecting to database failed\nError: ", error)
        time.sleep(5)




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
    cursor.execute("""SELECT * FROM Posts""")
    result=[]
    columns = [column[0] for column in cursor.description]
    for row in cursor.fetchall():
        result.append(dict(zip(columns,row)))
    return {"data": result}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    if post.published == True:
        post.published = 1
    else:
        post.published = 0

    cursor.execute(f"""INSERT INTO Posts (tittle, description, published) VALUES ('{post.tittle}', '{post.content}', {post.published})""")
    cnxn.commit()

    cursor.execute(f"""SELECT * FROM Posts WHERE id = SCOPE_IDENTITY()""")
    columns = [column[0] for column in cursor.description]
    result=[]
    row = cursor.fetchone()
    result=dict(zip(columns, row))

    return {"data": result}

@app.get("/posts/{id}")
def get_post(id: int):
    cursor.execute(f"""SELECT * FROM Posts WHERE id = {id}""")
    columns = [column[0] for column in cursor.description]
    result=[]
    row = cursor.fetchone()
    if not row:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    result=dict(zip(columns, row))
    return{"data":result}

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
