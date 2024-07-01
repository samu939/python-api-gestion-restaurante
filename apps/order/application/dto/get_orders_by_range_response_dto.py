from uuid import UUID

from core.infrastructure.utils.schemas_base import BaseSchema


class GetOrderPlateByIdResponse(BaseSchema):
    id: UUID
    name: str
    quantity: float
    
class GetOrdersByRangeResponse(BaseSchema):
    id: UUID
    date: str
    user: str
    price: float
    plates: list[GetOrderPlateByIdResponse]