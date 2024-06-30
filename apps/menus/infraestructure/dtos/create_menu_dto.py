from uuid import UUID
from pydantic import BaseModel


class CreateMenuDto(BaseModel):
    name: str
    plates: list[UUID]