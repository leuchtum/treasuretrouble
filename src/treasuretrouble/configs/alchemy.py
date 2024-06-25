from advanced_alchemy.extensions.litestar import AsyncSessionConfig
from advanced_alchemy.extensions.litestar import SQLAlchemyAsyncConfig
from advanced_alchemy.extensions.litestar import async_autocommit_before_send_handler

from treasuretrouble.settings import get_settings

settings = get_settings()
cfg = SQLAlchemyAsyncConfig(
    engine_instance=settings.db.get_engine(),
    before_send_handler=async_autocommit_before_send_handler,
    session_config=AsyncSessionConfig(expire_on_commit=False),
)
