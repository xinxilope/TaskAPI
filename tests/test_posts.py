from typing import List
from app import schemas
import pytest

def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get("/posts/")
    def validate(post):
        return schemas.Post(**post)
    post_map = list(map(validate, res.json()))

    assert len(res.json()) == len(test_posts)
    assert res.status_code == 200


def test_unauthorized_user_get_all_posts(client, test_posts):
    res = client.get("/posts/")

    assert res.status_code == 401


def test_unauthorized_user_get_one_posts(client, test_posts):
    res = client.get(f"/posts/{test_posts[0].POS_ID}")

    assert res.status_code == 401


def test_get_one_post_not_exist(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/565656")

    assert res.status_code == 404


def test_get_one_post(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/{test_posts[0].POS_ID}")
    post = schemas.Post(**res.json())

    assert post.POS_ID  == test_posts[0].POS_ID
    assert res.status_code == 200


@pytest.mark.parametrize("POS_TITLE, POS_DESCRIPTION, POS_PUBLISHED", [
    ("titutlo1", "decsrcao1", True),
    ("titut22", "dec2rca22", False),
    ("t3", "d3", True)
])
def test_create_post(authorized_client, test_user, POS_TITLE, POS_DESCRIPTION, POS_PUBLISHED):
    res = authorized_client.post("/posts/", json={"POS_TITLE": POS_TITLE, "POS_DESCRIPTION": POS_DESCRIPTION, "POS_PUBLISHED": POS_PUBLISHED})
    created_post = schemas.Post(**res.json())

    assert res.status_code == 201
    assert created_post.POS_TITLE == POS_TITLE
    assert created_post.POS_DESCRIPTION == POS_DESCRIPTION
    assert created_post.POS_PUBLISHED == POS_PUBLISHED


def test_create_post_default_published(authorized_client, test_user):
    res = authorized_client.post("/posts/", json={"POS_TITLE": "titulo", "POS_DESCRIPTION": "desc"})
    created_post = schemas.Post(**res.json())

    assert res.status_code == 201
    assert created_post.POS_TITLE == "titulo"
    assert created_post.POS_DESCRIPTION == "desc"
    assert created_post.POS_PUBLISHED == True


def test_create_post_unauthorized(client, test_user):
    res = client.post("/posts/", json={"POS_TITLE": "titulo", "POS_DESCRIPTION": "desc"})

    assert res.status_code == 401


def test_delete_post_sucess(authorized_client, test_user, test_posts):
    res = authorized_client.delete(f"/posts/{test_posts[0].POS_ID}")

    assert res.status_code == 204