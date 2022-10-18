from fastapi import Body, FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": "this is all your posts"}

@app.post("/createposts")
def create_posts(payload: dict = Body(...)): #desconstroi o body do POST, cria um dict e salva em payload
    print(payload)
    return {"new_post": f"title: {payload['tittle']} -- content: {payload['content']}"}