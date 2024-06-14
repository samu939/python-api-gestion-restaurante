from uuid import UUID
from core.infrastructure.utils.schemas_base import BaseSchema

class StoreIngredient (BaseSchema):
    id: UUID
    name: str
    quantity: float

class GetStoreByIdResponseDto (BaseSchema):
    id: UUID
    name: str
    ingredients: list[StoreIngredient]