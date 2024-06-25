from dataclasses import dataclass
from dataclasses import field

from dynaconf import Dynaconf
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import create_async_engine

_settings = Dynaconf(
    envvar_prefix="TT_DB",
    env_switcher="TT_ENV",
    settings_files=["tt_db.toml"],
    environments=True,
    env="default",
)


@dataclass
class DatabaseSettings:
    """Database settings for TreasureTrouble."""

    ENV: str = _settings.current_env
    URL: str = field(default_factory=lambda: _settings["url"])
    _engine_instance: AsyncEngine | None = None

    def _produce_engine(self) -> AsyncEngine:
        return create_async_engine(self.URL)

    def get_engine(self) -> AsyncEngine:
        """Get the SQLAlchemy engine."""
        if self._engine_instance is None:
            self._engine_instance = self._produce_engine()
        return self._engine_instance
