from uuid import UUID
from core.infrastructure.utils.schemas_base import BaseSchema


class GetMenuResponse(BaseSchema):
    id: UUID
    name: str

class GetAllMenusResponse(BaseSchema):
    menus: list[GetMenuResponse]