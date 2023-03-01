from app import schemas
from .database import client, session


def test_root(client):
    res = client.get("/")
    assert res.json().get("message") == "Welcome to Home Page!"
    assert res.status_code == 200


def test_create_user(client):
    res = client.post("/users/", json={"USU_EMAIL": "teste@mail.com", "USU_PASSWORD": "123456"})
    new_user = schemas.UserOut(**res.json())

    assert res.status_code == 201
    assert new_user.USU_EMAIL == "teste@mail.com"