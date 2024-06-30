

from uuid import UUID
from core.infrastructure.utils.schemas_base import BaseSchema


class Notification(BaseSchema):
    id: UUID
    message: str
    date: str
    target_user: UUID
    
class GetAllUserNotificationsResponse(BaseSchema):
    notifications: list[Notification]