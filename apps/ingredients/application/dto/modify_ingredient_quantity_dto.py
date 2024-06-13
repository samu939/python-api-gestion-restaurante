

from uuid import UUID
from pydantic import BaseModel


class ModifyIngredientQuantityDto(BaseModel):
    ingredient_id: UUID
    quantity: float