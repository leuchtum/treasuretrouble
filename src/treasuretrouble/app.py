from litestar import Litestar
from litestar.di import Provide

from treasuretrouble.configs.openapi import config as openapi_config
from treasuretrouble.lib.dependencies import provide_limit_offset_pagination
from treasuretrouble.server.plugins import active_plugins
from treasuretrouble.server.routers import route_handlers
from treasuretrouble.settings import get_settings

settings = get_settings()


limit_offset_dep = Provide(provide_limit_offset_pagination)


app = Litestar(
    openapi_config=openapi_config,
    route_handlers=route_handlers,
    plugins=active_plugins,
    dependencies={
        "limit_offset": limit_offset_dep,
    },
    debug=settings.app.DEBUG,
)
