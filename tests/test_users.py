import pytest
from jose import jwt
from app import schemas
from app.config import settings


@pytest.fixture()
def test_user(client):
    user_data = {"email": "create_user@test.com", "password": "create_user_test"}
    response = client.post("/user/", json=user_data)
    assert response.status_code == 201
    new_user = response.json()
    new_user["password"] = user_data["password"]
    return new_user


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


def test_login_user(client, test_user):
    response = client.post(
        "/login",
        data={"username": test_user["email"], "password": test_user["password"]},
    )
    login_res = schemas.Token(**response.json())
    payload = jwt.decode(
        login_res.access_token, settings.secret_key, algorithms=[settings.algorithm]
    )
    user_id: str = payload.get("user_id")
    assert user_id == test_user["id"]
    assert login_res.token_type == "bearer"
    assert response.status_code == 200
