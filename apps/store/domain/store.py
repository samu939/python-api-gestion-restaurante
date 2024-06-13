

from typing import List
from apps.ingredients.domain.value_objects.ingredient_id import IngredientId
from apps.store.domain.events.store_created import StoreCreatedEvent
from apps.store.domain.value_objects.store_id import StoreId
from apps.store.domain.value_objects.store_name import StoreName
from core.domain.aggregates.aggregate import Aggregate

class Inventory (Aggregate[StoreId]):
    def __init__(self, id: StoreId, name: StoreName, ingredients: List[IngredientId]) -> None:
        super().__init__(id)
        self.name = name
        self.ingredients = ingredients
        self.on(StoreCreatedEvent(id, name, ingredients))
        
    def validate_state(self) -> None:
        self.id.ensureValidState()
        self.name.ensureValidState()
        
    