

from pydantic import BaseModel


class CreateStoreEntry (BaseModel):
    name: str