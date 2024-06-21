"""Configuration module for TreasureTrouble."""

from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="TT",
    settings_files=["settings.toml", ".secrets.toml"],
    environments=True,
    env="default",
)
