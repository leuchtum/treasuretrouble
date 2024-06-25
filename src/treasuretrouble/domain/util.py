from contextlib import contextmanager
from typing import Iterator

import advanced_alchemy.exceptions
import litestar.exceptions


@contextmanager
def convert_repository_exceptions() -> Iterator[None]:
    try:
        yield
    except advanced_alchemy.exceptions.NotFoundError as e:
        raise litestar.exceptions.NotFoundException from e
