

from pydantic import BaseModel


class CreateIngredientDto (BaseModel):
    name: str
    quantity: int
    storeID: str