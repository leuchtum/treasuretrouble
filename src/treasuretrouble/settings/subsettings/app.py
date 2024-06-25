from dataclasses import dataclass
from dataclasses import field

from dynaconf import Dynaconf

_settings = Dynaconf(
    envvar_prefix="TT_APP",
    env_switcher="TT_ENV",
    settings_files=["tt_app.toml"],
    environments=True,
    env="default",
)


@dataclass(frozen=True)
class AppSettings:
    """App settings for TreasureTrouble."""

    ENV: str = _settings.current_env
    DEBUG: bool = field(default_factory=lambda: _settings["debug"])
    NAME: str = field(default_factory=lambda: _settings["name"])
