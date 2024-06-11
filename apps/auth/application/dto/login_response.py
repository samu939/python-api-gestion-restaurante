
from uuid import UUID

from core.infrastructure.utils.schemas_base import BaseSchema


class AuthResponse(BaseSchema):
    access_token: str
    token_type: str
    id: UUID
    name: str
    username: str
    role: str