from dataclasses import dataclass
from dataclasses import field

from dynaconf import Dynaconf

_settings = Dynaconf(
    envvar_prefix="TT_LOG",
    env_switcher="TT_ENV",
    settings_files=["tt_log.toml"],
    environments=True,
    env="default",
)


@dataclass(frozen=True)
class LogSettings:
    """Log settings for TreasureTrouble."""

    ENV: str = _settings.current_env
    LEVEL: int = field(default=_settings["level"])
    UVICORN_LEVEL: int = field(default=_settings["uvicorn_level"])
    SQLALCHEMY_LEVEL: int = field(default=_settings["sqlalchemy_level"])
