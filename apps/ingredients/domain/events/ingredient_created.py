from apps.ingredients.domain.value_objects.ingredient_id import IngredientId
from apps.ingredients.domain.value_objects.ingredient_name import IngredientName
from apps.ingredients.domain.value_objects.ingredient_quantity import IngredientQuantity
from apps.store.domain.value_objects.store_id import StoreId
from core.domain.events.domain_event import DomainEvent

class IngredientCreatedEvent(DomainEvent):
    def __init__(self, ingredient_id: IngredientId, ingredient_name: IngredientName, ingredient_quantity: IngredientQuantity, store_id: StoreId) -> None:
        super().__init__()
        self.ingredient_id = ingredient_id
        self.ingredient_name = ingredient_name
        self.ingredients_quantity = ingredient_quantity
        self.store_id = store_id
        