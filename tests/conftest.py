from collections.abc import Iterator

import pytest
from litestar import Litestar
from litestar.testing import TestClient
from treasuretrouble.app import app
from treasuretrouble.settings.subsettings.app import _settings as app_settings
from treasuretrouble.settings.subsettings.db import _settings as db_settings
from treasuretrouble.settings.subsettings.log import _settings as logging_settings
from treasuretrouble.settings.subsettings.server import _settings as server_settings


@pytest.fixture(scope="session", autouse=True)
def set_test_settings() -> None:
    """Set the environment to testing for all tests."""
    for settings in (app_settings, db_settings, logging_settings, server_settings):
        settings.configure(FORCE_ENV_FOR_DYNACONF="testing")


@pytest.fixture(scope="function")
def test_client() -> Iterator[TestClient[Litestar]]:
    with TestClient(app=app) as client:
        client.app.db_session
        yield client
