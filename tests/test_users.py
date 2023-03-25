from app import schemas
from tests.database import client, session


def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_create_user(client):
    response = client.post(
        "/user/", json={"email": "test@test.com", "password": "test"}
    )
    new_user = schemas.UserOut(**response.json())
    assert response.status_code == 201
    assert new_user.email == "test@test.com"
