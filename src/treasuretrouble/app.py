from litestar import Litestar
from litestar.contrib.sqlalchemy.base import BigIntBase
from litestar.contrib.sqlalchemy.plugins import AsyncSessionConfig
from litestar.contrib.sqlalchemy.plugins import SQLAlchemyAsyncConfig
from litestar.contrib.sqlalchemy.plugins import SQLAlchemyInitPlugin
from litestar.di import Provide

from treasuretrouble.config import settings
from treasuretrouble.database.pagination import provide_limit_offset_pagination
from treasuretrouble.database.users.controller import UserController
from treasuretrouble.logging import get_logger
from treasuretrouble.logging import logging_config
from treasuretrouble.version import __version__

session_config = AsyncSessionConfig(expire_on_commit=False)
sqlalchemy_config = SQLAlchemyAsyncConfig(
    connection_string=settings["database_url"],
    session_config=session_config,
)  # Create 'db_session' dependency.
sqlalchemy_plugin = SQLAlchemyInitPlugin(config=sqlalchemy_config)
limit_offset_dep = Provide(provide_limit_offset_pagination)


async def log_info() -> None:
    logger = get_logger()
    logger.info(f"Treasure Trouble version: {__version__}")
    logger.info(f"Running in '{settings.current_env}' environment.")


async def init_db() -> None:
    """Initializes the database."""
    async with sqlalchemy_config.get_engine().begin() as conn:
        await conn.run_sync(BigIntBase.metadata.create_all)


app = Litestar(
    route_handlers=[UserController],
    on_startup=[log_info, init_db],
    plugins=[sqlalchemy_plugin],
    dependencies={"limit_offset": limit_offset_dep},
    debug=settings["debug"],
    logging_config=logging_config,
)
