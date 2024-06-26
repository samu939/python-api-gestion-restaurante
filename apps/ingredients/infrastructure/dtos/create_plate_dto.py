from uuid import UUID
from pydantic import BaseModel

class IngredientsForPlate (BaseModel):
    id: UUID
    quantity: float

class CreatePlateDto (BaseModel):
    name: str
    description: str
    price: float
    ingredients: list[IngredientsForPlate]