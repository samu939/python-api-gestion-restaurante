from uuid import UUID
from pydantic import BaseModel

class ModifyMenuEntry(BaseModel):
    name: str
    plates: list[UUID]