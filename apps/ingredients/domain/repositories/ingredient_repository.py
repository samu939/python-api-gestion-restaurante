from abc import abstractmethod
from typing import Awaitable, List, Optional

from apps.ingredients.domain.ingredient import Ingredient
from apps.ingredients.domain.value_objects.ingredient_id import IngredientId

class IngredientRepository:
    @abstractmethod
    def get_ingredient_by_id(self, id: IngredientId) -> Awaitable[Optional[Ingredient]]:
        pass
    @abstractmethod
    def save_ingredient(self, ingredient: Ingredient) -> Awaitable[None]:
        pass
