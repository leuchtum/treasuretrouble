from dataclasses import dataclass

from dynaconf import Dynaconf

_settings = Dynaconf(
    envvar_prefix="TT_SERVER",
    env_switcher="TT_ENV",
    settings_files=["tt_server.toml"],
    environments=True,
    env="default",
)


@dataclass(frozen=True)
class ServerSettings:
    """Server settings for TreasureTrouble."""

    ENV: str = _settings.current_env
