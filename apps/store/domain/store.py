

from apps.ingredients.domain.value_objects.ingredient_id import IngredientId
from apps.store.domain.events.store_created import StoreCreatedEvent
from apps.store.domain.value_objects.store_id import StoreId
from apps.store.domain.value_objects.store_name import StoreName
from core.domain.aggregates.aggregate import Aggregate

class Store (Aggregate[StoreId]):
    def __init__(self, id: StoreId, name: StoreName) -> None:
        super().__init__(id)
        self.name = name
        self.on(StoreCreatedEvent(id, name))
        
    def validate_state(self) -> None:
        self.id.ensureValidState()
        self.name.ensureValidState()
        

        
        
        
    