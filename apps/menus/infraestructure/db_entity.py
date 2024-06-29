from uuid import UUID
from core.infrastructure.utils.schemas_base import BaseSchema

class Plate:
    id: UUID
    name: str
    price: float

class Menu(BaseSchema):
    id: UUID
    name: str
    plates: list[Plate]

