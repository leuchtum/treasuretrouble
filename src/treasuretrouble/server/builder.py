from __future__ import annotations

from typing import TYPE_CHECKING

from litestar import Litestar
from litestar.contrib.sqlalchemy.base import BigIntBase
from litestar.plugins import CLIPluginProtocol
from litestar.plugins import InitPluginProtocol

from treasuretrouble.settings import get_settings

if TYPE_CHECKING:
    from click import Group
    from litestar.config.app import AppConfig

from treasuretrouble.version import __version__


class ApplicationConfigurator(InitPluginProtocol, CLIPluginProtocol):
    def __init__(self) -> None:
        pass

    def on_cli_init(self, cli: Group) -> None:
        pass

    def on_app_init(self, app_config: AppConfig) -> AppConfig:
        app_config.on_startup.extend([_create_tables, _log_infos])

        return app_config


async def _create_tables() -> None:
    settings = get_settings()
    async with settings.db.get_engine().begin() as conn:
        await conn.run_sync(BigIntBase.metadata.create_all)


async def _log_infos(app: Litestar) -> None:
    settings = get_settings()
    if app.logger is None:
        return
    app.logger.info(f"Running in environment: {settings.environment}")
    app.logger.info(f"Treasure Trouble version: {__version__}")
