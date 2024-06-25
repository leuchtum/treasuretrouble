from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from functools import lru_cache

from treasuretrouble.settings.subsettings.app import AppSettings
from treasuretrouble.settings.subsettings.db import DatabaseSettings
from treasuretrouble.settings.subsettings.log import LogSettings
from treasuretrouble.settings.subsettings.server import ServerSettings


@dataclass(frozen=True)
class GlobalSettings:
    app: AppSettings = field(default_factory=AppSettings)
    db: DatabaseSettings = field(default_factory=DatabaseSettings)
    server: ServerSettings = field(default_factory=ServerSettings)
    log: LogSettings = field(default_factory=LogSettings)

    @classmethod
    def load(cls) -> GlobalSettings:
        return GlobalSettings()

    @property
    def environment(self) -> str:
        envs = {self.app.ENV, self.db.ENV, self.server.ENV, self.log.ENV}
        if len(envs) == 1:
            return envs.pop()
        raise ValueError("Multiple environments detected.")


@lru_cache(maxsize=1, typed=True)
def get_settings() -> GlobalSettings:
    return GlobalSettings.load()
