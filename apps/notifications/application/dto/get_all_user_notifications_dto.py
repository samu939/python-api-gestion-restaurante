


from uuid import UUID
from pydantic import BaseModel


class GetAllUserNotificationsDto(BaseModel):
    user_id: UUID