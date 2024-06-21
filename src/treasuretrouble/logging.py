import structlog

from treasuretrouble.config import settings
from treasuretrouble.version import __version__

logger = structlog.get_logger()

logger.info(f"Running in '{settings.current_env}' environment.")
logger.info(f"Version: {__version__}")
