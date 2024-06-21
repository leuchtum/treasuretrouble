from treasuretrouble.config import settings


def test_dynaconf_is_in_testing_env() -> None:
    """Test that Dynaconf is in the testing environment."""
    assert settings.current_env == "testing"
