from uuid import UUID
from pydantic import BaseModel

class IngredientsForPlate (BaseModel):
    id: UUID
    quantity: float

class ModifyPlateDto (BaseModel):
    id: UUID
    price: float
    ingredients: list[IngredientsForPlate]