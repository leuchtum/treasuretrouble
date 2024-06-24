import random

from litestar import Litestar
from litestar.status_codes import HTTP_200_OK
from litestar.status_codes import HTTP_202_ACCEPTED
from litestar.testing import TestClient

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def new_user(test_client: TestClient[Litestar]) -> int:
    random_username = "".join(random.choice(ALPHABET) for _ in range(10))
    data = {"name": random_username}
    response = test_client.post("/users", json=data)
    assert response.status_code == HTTP_202_ACCEPTED
    return response.json()["id"]


def test_create_user(test_client: TestClient[Litestar]) -> None:
    response = test_client.get("/users")
    assert response.status_code == HTTP_200_OK
    assert response.json() == {"items": [], "limit": 10, "offset": 0, "total": 0}

    user_id = new_user(test_client)
    assert response.status_code == HTTP_202_ACCEPTED
    assert response.json() == {"name": "testuser"}
