from litestar.contrib.sqlalchemy.repository import SQLAlchemyAsyncRepository
from sqlalchemy.ext.asyncio import AsyncSession

from treasuretrouble.database.models import UserModel


class UserRepository(SQLAlchemyAsyncRepository[UserModel]):
    model_type = UserModel


async def provide_users_repo(db_session: AsyncSession) -> UserRepository:
    return UserRepository(session=db_session)
