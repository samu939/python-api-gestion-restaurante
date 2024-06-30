

from uuid import UUID
from pydantic import BaseModel


class SaveNotificationDto (BaseModel):
    message: str
    target_user: UUID