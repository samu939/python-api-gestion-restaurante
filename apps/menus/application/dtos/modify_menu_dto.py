from uuid import UUID
from pydantic import BaseModel


class ModifyMenuDto(BaseModel):
    id: UUID
    name: str
    plates: list[UUID]