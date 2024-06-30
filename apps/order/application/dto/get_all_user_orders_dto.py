


from uuid import UUID
from pydantic import BaseModel


class GetAllUserOrdersDto (BaseModel):
    user_id: UUID