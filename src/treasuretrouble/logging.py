import structlog

from treasuretrouble import settings

logger = structlog.get_logger()

logger.info(f"Running in '{settings.current_env}' environment.")
