from enum import Enum
from uuid import UUID

from core.infrastructure.utils.schemas_base import BaseSchema

class roleEnum (str,Enum):
    administrador = "administrador"
    camarero = "camarero"
    chef = "chef"
    cliente = "cliente"

class UserInDB (BaseSchema):
    id: UUID
    name: str
    password: str
    role: roleEnum
    username: str