from app import schemas
from jose import jwt
from app.config import settings
import pytest


# def test_root(client):
#     res = client.get("/")
#     assert res.json().get("message") == "Welcome to Home Page!"
#     assert res.status_code == 200


def test_create_user(client):
    res = client.post("/users/", json={"USU_EMAIL": "teste@mail.com", "USU_PASSWORD": "123456"})
    new_user = schemas.UserOut(**res.json())

    assert res.status_code == 201
    assert new_user.USU_EMAIL == "teste@mail.com"


def test_login_user(test_user, client):
    res = client.post("/login", data={"username": test_user['USU_EMAIL'], "password": test_user['USU_PASSWORD']})
    login_res = schemas.Token(**res.json())

    payload = jwt.decode(login_res.access_token, settings.TASKAPI_SECRET_KEY, algorithms=[settings.TASKAPI_ALGORITHM])
    id = payload.get("user_id")

    assert id == test_user["USU_ID"]
    assert login_res.token_type == "bearer"
    assert res.status_code == 200


@pytest.mark.parametrize("email, password, status_code",[
    ('teste2222@mail.com', 'passwro', 403),
    ('teste2222@mail.com', 'asdasda', 403),
    ('teste2222@mail.com', 'ttttttt', 403),
    (None, 'ttttt', 422),
    ('teste2222@mail.com', None, 422)
])
def test_wrong_login_user(client, email, password, status_code):
    res = client.post("/login", data={"username": email, "password": password})

    assert res.status_code == status_code