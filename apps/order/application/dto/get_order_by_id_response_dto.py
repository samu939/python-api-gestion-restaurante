from uuid import UUID

from core.infrastructure.utils.schemas_base import BaseSchema


class GetOrderPlateByIdResponse(BaseSchema):
    id: UUID
    name: str
    quantity: float
    
class GetOrderByIdResponse(BaseSchema):
    id: UUID
    date: str
    user_id: UUID
    price: float
    plates: list[GetOrderPlateByIdResponse]