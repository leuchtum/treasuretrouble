from treasuretrouble.config import settings


def test_dynaconf_is_in_testing_env() -> None:
    assert settings.current_env == "testing"
