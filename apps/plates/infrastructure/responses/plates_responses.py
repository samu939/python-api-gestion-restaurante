from uuid import UUID
from core.infrastructure.utils.schemas_base import BaseSchema


class GetPlatesIngredientResponse(BaseSchema):
    id: UUID
    quantity: float



class GetPlateResponse(BaseSchema):
    id: UUID
    name: str
    description: str
    price: float
    ingredients: list[GetPlatesIngredientResponse]

class GetAllPlatesResponse(BaseSchema):
    plates: list[GetPlateResponse]

class SavePlateResponse(BaseSchema):
    response: str