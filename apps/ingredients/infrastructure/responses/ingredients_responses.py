

from uuid import UUID
from core.infrastructure.utils.schemas_base import BaseSchema


class GetIngredientResponse(BaseSchema):
    id: UUID
    name: str