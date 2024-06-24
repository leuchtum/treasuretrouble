from collections.abc import Iterator

import pytest
from litestar import Litestar
from litestar.testing import TestClient
from treasuretrouble.app import app
from treasuretrouble.config import settings


@pytest.fixture(scope="session", autouse=True)
def set_test_settings() -> None:
    """Set the environment to testing for all tests."""
    settings.configure(FORCE_ENV_FOR_DYNACONF="testing")


@pytest.fixture(scope="function")
def test_client() -> Iterator[TestClient[Litestar]]:
    with TestClient(app=app) as client:
        client.app.db_session
        yield client
