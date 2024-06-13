
from apps.ingredients.domain.value_objects.ingredient_id import IngredientId
from typing import List
from apps.store.domain.value_objects.store_id import StoreId
from apps.store.domain.value_objects.store_name import StoreName
from core.domain.events.domain_event import DomainEvent

class StoreCreatedEvent(DomainEvent):
    def __init__(self, store_id: StoreId, store_name: StoreName, ingredients: List[IngredientId]) -> None:
        super().__init__()
        self.store_id = store_id
        self.store_name = store_name
        self.ingredients = ingredients