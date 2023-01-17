from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
import pyodbc, os, time


app = FastAPI()


class Post(BaseModel):
    title: str
    description: str
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



@app.get("/")
def root():
    return {"message": "Welcome to Home Page!"}

@app.get("/posts")
def get_posts():
    result=[]

    cursor.execute("""SELECT * FROM POSTS""")
    columns = [column[0] for column in cursor.description]
    for row in cursor.fetchall():
        result.append(dict(zip(columns,row)))

    return {"data": result}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    result=[]

    if post.published == True:
        post.published = 1
    else:
        post.published = 0

    cursor.execute("""INSERT INTO POSTS (POS_TITLE, POS_DESCRIPTION, POS_PUBLISHED) OUTPUT Inserted.* VALUES (?, ?, ?)""",post.title,post.description,post.published)
    columns = [column[0] for column in cursor.description]
    row = cursor.fetchone()
    result=dict(zip(columns, row))
    cnxn.commit()

    return {"data": result}

@app.get("/posts/{id}")
def get_post(id: int):
    result=[]

    cursor.execute("""SELECT * FROM POSTS WHERE POS_ID = ?""", id)
    columns = [column[0] for column in cursor.description]
    row = cursor.fetchone()
    if not row:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    result=dict(zip(columns, row))

    return{"data":result}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):

    cursor.execute("""DELETE FROM POSTS OUTPUT Deleted.* WHERE POS_ID = ?""", id)
    row = cursor.fetchone()
    if not row:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    cnxn.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    result=[]

    if post.published == True:
        post.published = 1
    else:
        post.published = 0

    cursor.execute("""UPDATE POSTS SET POS_TITLE = ?,POS_DESCRIPTION = ?,POS_PUBLISHED = ? OUTPUT Inserted.* WHERE POS_ID = ?""", post.title,post.description,post.published,id)
    columns = [column[0] for column in cursor.description]
    row = cursor.fetchone()
    if not row:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    result=dict(zip(columns, row))
    cnxn.commit()

    return{"data":result}

