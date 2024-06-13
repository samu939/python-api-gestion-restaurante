from abc import abstractmethod
from ast import Store
from typing import Awaitable, Optional
from apps.store.domain.value_objects.store_id import StoreId


class StoreRepository:
    @abstractmethod
    def get_store_by_id(self, id: StoreId) -> Awaitable[Optional[Store]]:
        pass