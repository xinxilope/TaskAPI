import pytest
from app import models

@pytest.fixture()
def test_like(test_posts, session, test_user):
    new_like = models.Likes(LIK_POS_ID=test_posts[1].POS_ID, LIK_USU_ID=test_user['USU_ID'])
    session.add(new_like)
    session.commit()


def test_like_on_post(authorized_client, test_posts):
    res = authorized_client.post("/like/", json={"post_id": test_posts[0].POS_ID, "dir": 1})
    assert res.status_code == 201


def test_like_twice_post(authorized_client, test_posts, test_like):
    res = authorized_client.post("/like/", json={"post_id": test_posts[1].POS_ID, "dir": 1})

    assert res.status_code == 409