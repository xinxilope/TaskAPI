from fastapi import FastAPI, Depends
from . import models
from .database import engine
from .routers import post, user, auth, likes
from sqlalchemy.orm import Session
from .database import get_db


# comando desnecessario pois o Almebic cuida da database
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(likes.router)

@app.get("/")
def root():
    return {"message": "Welcome to Home Page!"}


@app.post("/query_generica")
def query_generica(query: str, db: Session = Depends(get_db)):

    result = db.execute(query).all()

    return result
