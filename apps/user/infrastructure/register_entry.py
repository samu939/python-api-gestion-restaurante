from pydantic import BaseModel
from apps.user.infrastructure.db_entity.user_in_db import roleEnum


class RegisterUserEntry(BaseModel):
    name: str
    password: str
    role: roleEnum
    username: str