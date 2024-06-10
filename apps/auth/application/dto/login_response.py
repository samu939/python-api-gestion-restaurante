
from uuid import UUID


class AuthResponse():
    access_token: str
    token_type: str
    id: UUID
    name: str
    username: str
    role: str