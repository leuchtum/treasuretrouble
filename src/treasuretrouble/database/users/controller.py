from litestar.controller import Controller
from litestar.di import Provide
from litestar.handlers.http_handlers.decorators import delete
from litestar.handlers.http_handlers.decorators import get
from litestar.handlers.http_handlers.decorators import patch
from litestar.handlers.http_handlers.decorators import post
from litestar.pagination import OffsetPagination
from litestar.params import Parameter
from litestar.repository.filters import LimitOffset
from pydantic import TypeAdapter

from treasuretrouble.database.models import User
from treasuretrouble.database.models import UserCreate
from treasuretrouble.database.models import UserModel
from treasuretrouble.database.models import UserUpdate
from treasuretrouble.database.users.repo import UserRepository
from treasuretrouble.database.users.repo import provide_users_repo
from treasuretrouble.database.util import convert_repository_exceptions


class UserController(Controller):
    """User CRUD"""

    dependencies = {"users_repo": Provide(provide_users_repo)}

    @get(path="/users")
    async def list_user(
        self,
        users_repo: UserRepository,
        limit_offset: LimitOffset,
    ) -> OffsetPagination[User]:
        """List users."""
        with convert_repository_exceptions():
            results, total = await users_repo.list_and_count(limit_offset)
        type_adapter = TypeAdapter(list[User])
        return OffsetPagination[User](
            items=type_adapter.validate_python(results),
            total=total,
            limit=limit_offset.limit,
            offset=limit_offset.offset,
        )

    @post(path="/users")
    async def create_user(
        self,
        users_repo: UserRepository,
        data: UserCreate,
    ) -> User:
        """Create a new user."""
        with convert_repository_exceptions():
            obj = await users_repo.add(
                UserModel(**data.model_dump(exclude_unset=True, exclude_none=True))
            )
        await users_repo.session.commit()
        return User.model_validate(obj)

    @get(path="/users/{user_id:int}")
    async def get_user(
        self,
        users_repo: UserRepository,
        user_id: int = Parameter(
            title="User ID",
            description="The user to retrieve.",
        ),
    ) -> User:
        """Get an existing user."""
        with convert_repository_exceptions():
            obj = await users_repo.get(user_id)
        return User.model_validate(obj)

    @patch(path="/users/{user_id:int}")
    async def update_user(
        self,
        users_repo: UserRepository,
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
            obj = await users_repo.update(UserModel(**as_dict))
        await users_repo.session.commit()
        return User.model_validate(obj)

    @delete(path="/users/{user_id:int}")
    async def delete_user(
        self,
        users_repo: UserRepository,
        user_id: int = Parameter(
            title="User ID",
            description="The user to delete.",
        ),
    ) -> None:
        """Delete a user from the system."""
        with convert_repository_exceptions():
            await users_repo.delete(user_id)
        await users_repo.session.commit()
