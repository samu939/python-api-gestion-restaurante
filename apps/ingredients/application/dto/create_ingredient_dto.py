

from pydantic import BaseModel


class CreateIngredientDto (BaseModel):
    name: str
    quantity: int
    store_id: str