

from uuid import UUID
from pydantic import BaseModel


class ModifyStoreEntry (BaseModel):
    store_id: UUID