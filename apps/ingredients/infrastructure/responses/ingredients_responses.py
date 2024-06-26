

from uuid import UUID
from core.infrastructure.utils.schemas_base import BaseSchema


class GetIngredientResponse(BaseSchema):
    id: UUID
    name: str
    quantity: float
    storeId: UUID | None 
    
class SaveIngredientResponse(BaseSchema):
    response: str
    
class GetAllIngredientsResponse(BaseSchema):
    ingredients: list[GetIngredientResponse]