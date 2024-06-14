from abc import abstractmethod
from typing import Awaitable, Optional

from apps.ingredients.domain.ingredient import Ingredient
from apps.ingredients.domain.value_objects.ingredient_id import IngredientId
from apps.store.domain.value_objects.store_id import StoreId

class IngredientRepository:
    @abstractmethod
    def get_ingredient_by_id(self, id: IngredientId) -> Awaitable[Optional[Ingredient]]:
        pass
    @abstractmethod
    def save_ingredient(self, ingredient: Ingredient) -> Awaitable[None]:
        pass
    @abstractmethod
    def get_all_ingredients(self) -> Awaitable[list[Ingredient]]:
        pass
    @abstractmethod
    def change_ingredient_store(self, id: IngredientId) -> Awaitable[None]:
        pass
    @abstractmethod
    def get_store_ingredients (self, id: StoreId) -> Awaitable [list[Ingredient]]:
        pass
    
