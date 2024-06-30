from uuid import UUID
from core.infrastructure.utils.schemas_base import BaseSchema

class MenuPlates(BaseSchema):
    id: UUID
    name: str
    price: float

class GetMenuWithPlatesResponse(BaseSchema):
    id: UUID
    name: str
    plates: list[MenuPlates]

class GetMenuResponse(BaseSchema):
    id: UUID
    name: str

class GetAllMenusResponse(BaseSchema):
    menus: list[GetMenuResponse]

class SaveMenuResponse(BaseSchema):
    response: str