from uuid import UUID
from core.infrastructure.utils.schemas_base import BaseSchema
from datetime import date


class NotificationInDB(BaseSchema):
    id: UUID
    message: str
    date: date
    target_user: UUID