from abc import abstractmethod
from typing import Awaitable, Optional
from apps.ingredients.domain.ingredient import Ingredient
from apps.ingredients.domain.value_objects.ingredient_id import IngredientId
from apps.store.domain.store import Store
from apps.store.domain.value_objects.store_id import StoreId


class StoreRepository:
    @abstractmethod
    def get_store_by_id(self, id: StoreId) -> Awaitable[Optional[Store]]:
        pass
    
    @abstractmethod
    def save_store(self, store: Store) -> Awaitable[None]:
        pass
    
    @abstractmethod
    def get_all_stores(self) -> Awaitable[list[Store]]:
        pass