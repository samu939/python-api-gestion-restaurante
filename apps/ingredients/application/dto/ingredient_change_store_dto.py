
from uuid import UUID
from pydantic import BaseModel


class IngredientChangeStoreDto(BaseModel):
    store_id: UUID
    ingredient_id: UUID
