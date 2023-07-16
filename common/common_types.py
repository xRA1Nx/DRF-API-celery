from __future__ import annotations

import typing

from django.db.models import Model

DjangoModel = typing.TypeVar('DjangoModel', bound=Model)
GenericContext = dict[str, typing.Any]
