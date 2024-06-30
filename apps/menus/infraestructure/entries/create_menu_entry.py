from uuid import UUID
from pydantic import BaseModel

class CreateMenuEntry(BaseModel):
    name: str
    plates: list[UUID]