
from apps.ingredients.domain.value_objects.ingredient_id import IngredientId
from apps.ingredients.domain.value_objects.ingredient_quantity import IngredientQuantity
from apps.store.domain.value_objects.store_id import StoreId
from core.domain.events.domain_event import DomainEvent

class IngredientChangedStoreEvent(DomainEvent):
    def __init__(self, ingredient_id: IngredientId, store_id: StoreId) -> None:
        super().__init__()
        self.ingredient_id = ingredient_id
        self.store_id = store_id
        