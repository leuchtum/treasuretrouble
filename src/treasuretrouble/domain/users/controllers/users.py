from __future__ import annotations

from advanced_alchemy.service import OffsetPagination
from litestar import Controller
from litestar import delete
from litestar import get
from litestar import patch
from litestar import post
from litestar.di import Provide
from litestar.params import Parameter
from litestar.repository.filters import LimitOffset
from pydantic import TypeAdapter

import treasuretrouble.domain.users.urls as urls
from treasuretrouble.database.models import UserModel
from treasuretrouble.domain.users.dependencies import provide_users_service
from treasuretrouble.domain.users.schemas import User
from treasuretrouble.domain.users.schemas import UserCreate
from treasuretrouble.domain.users.schemas import UserUpdate
from treasuretrouble.domain.users.services import UserService
from treasuretrouble.domain.util import convert_repository_exceptions


class UserController(Controller):
    """User CRUD"""

    dependencies = {"users_service": Provide(provide_users_service)}

    @get(path=urls.LIST_USERS)
    async def list_user(
        self,
        users_service: UserService,
        limit_offset: LimitOffset,
    ) -> OffsetPagination[User]:
        """List users."""
        with convert_repository_exceptions():
            results, total = await users_service.list_and_count(limit_offset)
        type_adapter = TypeAdapter(list[User])
        return OffsetPagination[User](
            items=type_adapter.validate_python(results),
            total=total,
            limit=limit_offset.limit,
            offset=limit_offset.offset,
        )

    @post(path=urls.CREATE_USER)
    async def create_user(
        self,
        users_service: UserService,
        data: UserCreate,
    ) -> User:
        """Create a new user."""
        with convert_repository_exceptions():
            obj = await users_service.create(
                UserModel(**data.model_dump(exclude_unset=True, exclude_none=True))
            )
        return User.model_validate(obj)

    @get(path=urls.GET_USER)
    async def get_user(
        self,
        users_service: UserService,
        user_id: int = Parameter(
            title="User ID",
            description="The user to retrieve.",
        ),
    ) -> User:
        """Get an existing user."""
        with convert_repository_exceptions():
            obj = await users_service.get(user_id)
        return User.model_validate(obj)

    @patch(path=urls.UPDATE_USER)
    async def update_user(
        self,
        users_service: UserService,
        data: UserUpdate,
        user_id: int = Parameter(
            title="User ID",
            description="The user to update.",
        ),
    ) -> User:
        """Update an user."""
        as_dict = data.model_dump(exclude_unset=True, exclude_none=True)
        as_dict.update({"id": user_id})
        with convert_repository_exceptions():
            obj = await users_service.update(UserModel(**as_dict))
        return User.model_validate(obj)

    @delete(path=urls.DELETE_USER)
    async def delete_user(
        self,
        users_service: UserService,
        user_id: int = Parameter(
            title="User ID",
            description="The user to delete.",
        ),
    ) -> None:
        """Delete a user from the system."""
        with convert_repository_exceptions():
            await users_service.delete(user_id)
