from treasuretrouble.settings import get_settings


def test_dynaconf_is_in_testing_env() -> None:
    """Test that Dynaconf is in the testing environment."""
    settings = get_settings()
    assert settings.environment == "testing"
