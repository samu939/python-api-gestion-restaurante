from uuid import UUID
from pydantic import BaseModel

class OrderPlateEntry (BaseModel):
    id: UUID
    quantity: float

class CreateOrderEntry (BaseModel):
    plates: list[OrderPlateEntry]
