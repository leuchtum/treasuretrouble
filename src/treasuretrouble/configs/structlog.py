import logging

from litestar.logging.config import LoggingConfig
from litestar.logging.config import StructLoggingConfig
from litestar.middleware.logging import LoggingMiddlewareConfig
from litestar.plugins.structlog import StructlogConfig

from treasuretrouble.settings import get_settings

settings = get_settings()
cfg = StructlogConfig(
    structlog_logging_config=StructLoggingConfig(
        log_exceptions="always",
        standard_lib_logging_config=LoggingConfig(
            root={
                "level": logging.getLevelName(settings.log.LEVEL),
                "handlers": ["queue_listener"],
            },
            loggers={
                "uvicorn": {
                    "propagate": False,
                    "level": settings.log.UVICORN_LEVEL,
                    "handlers": ["queue_listener"],
                },
                "uvicorn.access": {
                    "propagate": False,
                    "level": settings.log.UVICORN_LEVEL,
                    "handlers": ["queue_listener"],
                },
                "uvicorn.asgi": {
                    "propagate": False,
                    "level": settings.log.UVICORN_LEVEL,
                    "handlers": ["queue_listener"],
                },
                "uvicorn.error": {
                    "propagate": False,
                    "level": settings.log.UVICORN_LEVEL,
                    "handlers": ["queue_listener"],
                },
                "sqlalchemy.engine": {
                    "propagate": False,
                    "level": settings.log.SQLALCHEMY_LEVEL,
                    "handlers": ["queue_listener"],
                },
                "sqlalchemy.pool": {
                    "propagate": False,
                    "level": settings.log.SQLALCHEMY_LEVEL,
                    "handlers": ["queue_listener"],
                },
            },
        ),
    ),
    middleware_logging_config=LoggingMiddlewareConfig(
        request_log_fields=["method", "path", "path_params", "query", "body"],
        response_log_fields=["status_code"],
    ),
)
