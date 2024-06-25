from litestar.types import ControllerRouterHandler

from treasuretrouble.domain.users.controllers.users import UserController

route_handlers: list[ControllerRouterHandler] = [
    UserController,
]
