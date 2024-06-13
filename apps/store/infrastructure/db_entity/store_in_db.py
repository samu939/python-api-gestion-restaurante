
from uuid import UUID
from core.infrastructure.utils.schemas_base import BaseSchema


class StoreInDb (BaseSchema):
    id: UUID
    name: str
    ingredients: list[UUID]