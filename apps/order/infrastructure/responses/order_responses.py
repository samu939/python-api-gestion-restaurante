from uuid import UUID
from core.infrastructure.utils.schemas_base import BaseSchema


class GetOrderPlateResponse(BaseSchema):
    id: UUID
    quantity: float



class GetOrderResponse(BaseSchema):
    id: UUID
    date: str
    user_id: UUID
    price: float
    plates: list[GetOrderPlateResponse]

class GetAllOrdersResponse(BaseSchema):
    orders: list[GetOrderResponse]

class SaveOrderResponse(BaseSchema):
    response: str
    
