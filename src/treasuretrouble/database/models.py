from __future__ import annotations

from datetime import date

from litestar.contrib.sqlalchemy.base import BigIntAuditBase
from sqlalchemy.orm import Mapped


class UserModel(BigIntAuditBase):
    __tablename__ = "user"
    name: Mapped[str]
    dob: Mapped[date | None]
