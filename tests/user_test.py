from fastapi.testclient import TestClient
from app.database import get_db, Base
from app.main import app
from app import schemas
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pytest


####################################### USANDO DATABASE DE TESTES DO BANCO #######################################
engine = create_engine("mssql+pyodbc:///?odbc_connect=DRIVER={SQL+Server+Native+Client+11.0};SERVER=localhost;DATABASE=testtaskAPI;Trusted_Connection=yes")
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_test_db():
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = get_test_db
###################################################################################################################


@pytest.fixture
def client():
    # run before tests
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    # run tests
    yield TestClient(app)
    


def test_root(client):
    res = client.get("/")
    assert res.json().get("message") == "Welcome to Home Page!"
    assert res.status_code == 200


def test_create_user(client):
    res = client.post("/users/", json={"USU_EMAIL": "teste@mail.com", "USU_PASSWORD": "123456"})
    new_user = schemas.UserOut(**res.json())

    assert res.status_code == 201
    assert new_user.USU_EMAIL == "teste@mail.com"