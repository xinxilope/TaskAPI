from fastapi import FastAPI, Response, status, HTTPException, Depends
import pyodbc, os, time
from . import models, schemas, utils
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import post, user


models.Base.metadata.create_all(bind=engine)
app = FastAPI()



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




app.include_router(post.router)
app.include_router(user.router)

@app.get("/")
def root():
    return {"message": "Welcome to Home Page!"}
