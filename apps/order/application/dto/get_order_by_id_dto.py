
from uuid import UUID
from pydantic import BaseModel


class GetOrderByIdDto (BaseModel):
    id: UUID