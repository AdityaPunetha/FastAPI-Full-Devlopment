import pytest
from jose import jwt
from app import schemas
from app.config import settings


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


@pytest.mark.parametrize(
    "email, password, status_code",
    [
        ("wrong_email@gmail.com", "create_user_test", 403),
        ("create_user@test.com", "wrong_password", 403),
        ("wrong_email@gmail.com", "wrong_password", 403),
        (None, "create_user_test", 422),
        ("create_user@test.com", None, 422),
    ],
)
def test_incorrect_login(test_user, client, email, password, status_code):
    response = client.post(
        "/login",
        data={"username": email, "password": password},
    )
    assert response.status_code == status_code
    # assert response.json() == {"detail": "Invalid credentials"}
