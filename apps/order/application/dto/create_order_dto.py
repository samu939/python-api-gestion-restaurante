from uuid import UUID
from pydantic import BaseModel

class OrderPlate (BaseModel):
    id: UUID
    quantity: float

class CreateOrderDto (BaseModel):
    user_id: UUID
    plates: list[OrderPlate]