"""User Account Controllers."""

from __future__ import annotations

from typing import TYPE_CHECKING

from treasuretrouble.domain.users.services import UserService

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

    from sqlalchemy.ext.asyncio import AsyncSession


async def provide_users_service(
    db_session: AsyncSession,
) -> AsyncGenerator[UserService, None]:
    """Construct repository and service objects for the request."""
    async with UserService.new(session=db_session) as service:
        yield service
