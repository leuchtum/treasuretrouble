from __future__ import annotations

from datetime import date
from datetime import datetime

from treasuretrouble.lib.schema import BaseSchema


class User(BaseSchema):
    id: int | None
    name: str
    dob: date | None = None
    created_at: datetime
    updated_at: datetime


class UserCreate(BaseSchema):
    name: str
    dob: date | None = None


class UserUpdate(BaseSchema):
    name: str | None = None
    dob: date | None = None
