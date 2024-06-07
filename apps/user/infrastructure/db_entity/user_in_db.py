from enum import Enum

class roleEnum (str,Enum):
    administrador = "administrador"
    camarero = "camarero"
    chef = "chef"
    cliente = "cliente"

class UserInDB:
    def __init__(self, id: str, name: str, username: str, password: str, role: roleEnum) -> None:
        self.id = id
        self.name = name
        self.password = password
        self.role = role
        self.username = username