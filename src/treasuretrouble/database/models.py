from __future__ import annotations

from datetime import date
from datetime import datetime

import pydantic
from litestar.contrib.sqlalchemy.base import BigIntAuditBase
from sqlalchemy.orm import Mapped


class BaseModel(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid", from_attributes=True)


class UserModel(BigIntAuditBase):
    __tablename__ = "user"
    name: Mapped[str]
    dob: Mapped[date | None]


class User(BaseModel):
    id: int | None
    name: str
    dob: date | None = None
    created_at: datetime
    updated_at: datetime


class UserCreate(BaseModel):
    name: str
    dob: date | None = None


class UserUpdate(BaseModel):
    name: str | None = None
    dob: date | None = None
