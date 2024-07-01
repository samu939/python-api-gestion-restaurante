from uuid import UUID
from pydantic import BaseModel

class IngredientsForPlateEntry (BaseModel):
    id: UUID
    quantity: float

class ModifyPlateEntry (BaseModel):
    price: float
    ingredients: list[IngredientsForPlateEntry]
