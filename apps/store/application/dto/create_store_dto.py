

from pydantic import BaseModel


class CreateStoreDto (BaseModel):
    name: str