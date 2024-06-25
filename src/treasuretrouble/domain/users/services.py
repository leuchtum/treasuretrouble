from __future__ import annotations

from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService

from treasuretrouble.database.models import UserModel
from treasuretrouble.domain.users.repositories import UserRepository


class UserService(SQLAlchemyAsyncRepositoryService[UserModel]):
    """Handles database operations for users."""

    repository_type = UserRepository
