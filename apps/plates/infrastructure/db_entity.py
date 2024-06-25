from uuid import UUID
from core.infrastructure.utils.schemas_base import BaseSchema

class Ingredient (BaseSchema):
    id: UUID
    name: str
    quantity: int

class PlateInDB (BaseSchema):
    id: UUID
    name: str
    description: str
    price: UUID
    ingredients: list[Ingredient]
