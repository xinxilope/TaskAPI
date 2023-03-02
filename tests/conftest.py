from fastapi.testclient import TestClient
from app.database import get_db, Base
from app.main import app
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pytest
from app.oauth2 import create_acess_token
from app import models


# USANDO BANCO DE TESTES
engine = create_engine("mssql+pyodbc:///?odbc_connect=DRIVER={SQL+Server+Native+Client+11.0};SERVER=localhost;DATABASE=testtaskAPI;Trusted_Connection=yes")
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):
    def get_test_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = get_test_db
    yield TestClient(app)


@pytest.fixture
def test_user(client):
    user_data={"USU_EMAIL": "teste@mail.com", "USU_PASSWORD": "123456"}
    res=client.post("/users/", json=user_data)

    assert res.status_code == 201

    new_user = res.json()
    new_user['USU_PASSWORD'] = user_data['USU_PASSWORD']
    return new_user


@pytest.fixture
def token(test_user):
    return create_acess_token({"user_id": test_user['USU_ID']})


@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }

    return client


@pytest.fixture
def test_posts(test_user, session):
    posts_data = [{
        "POS_TITLE": "first test post",
        "POS_DESCRIPTION": "first test description",
        "POS_USU_ID": test_user['USU_ID']
    },
    {
        "POS_TITLE": "second test post",
        "POS_DESCRIPTION": "second test description",
        "POS_USU_ID": test_user['USU_ID']
    }]

    def create_post_model(post):
        return models.Post(**post)

    post_map = list(map(create_post_model, posts_data))

    session.add_all(post_map)
    session.commit()
    posts = session.query(models.Post).all()
    
    return posts