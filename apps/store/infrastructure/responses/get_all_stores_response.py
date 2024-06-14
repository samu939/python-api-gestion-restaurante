
from uuid import UUID
from pydantic import BaseModel

from apps.store.domain.store import Store

class StoreResponse (BaseModel):
    id: UUID
    name: str

class GetAllStoresResponse (BaseModel):
    stores: list[StoreResponse]