from uuid import UUID
from pydantic import BaseModel

class IngredientsForPlateEntry (BaseModel):
    id: UUID
    quantity: float

class CreatePlateEntry (BaseModel):
    name: str
    description: str
    price: float
    ingredients: list[IngredientsForPlateEntry]