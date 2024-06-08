

from uuid import UUID
from apps.user.infrastructure.db_entity.user_in_db import roleEnum
from core.infrastructure.utils.schemas_base import BaseSchema


class GetUserResponse(BaseSchema):
    id: UUID
    name: str
    username: str
    password: str
    role: roleEnum