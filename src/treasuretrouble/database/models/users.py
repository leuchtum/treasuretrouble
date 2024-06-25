from __future__ import annotations

from datetime import date

from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy.orm import Mapped


class User(UUIDAuditBase):
    __tablename__ = "user"
    name: Mapped[str]
    dob: Mapped[date | None]
