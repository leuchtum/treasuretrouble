import pytest
from treasuretrouble.config import settings


@pytest.fixture(scope="session", autouse=True)
def set_test_settings() -> None:
    """Set the environment to testing for all tests."""
    settings.configure(FORCE_ENV_FOR_DYNACONF="testing")
