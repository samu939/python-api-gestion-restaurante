


from uuid import UUID

from pydantic import BaseModel


class GetStoreResponse (BaseModel):
    id: UUID
    name: str
    ingredients: list[UUID]