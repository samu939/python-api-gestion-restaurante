from apps.ingredients.domain.value_objects.ingredient_id import IngredientId
from apps.ingredients.domain.value_objects.ingredient_name import IngredientName
from apps.ingredients.domain.value_objects.ingredient_quantity import IngredientQuantity
from core.domain.events.domain_event import DomainEvent

class IngredientQuantityUpdatedEvent(DomainEvent):
    def __init__(self, ingredient_id: IngredientId, ingredient_name: IngredientName, ingredient_quantity: IngredientQuantity) -> None:
        super().__init__()
        self.ingredient_id = ingredient_id
        self.ingredient_name = ingredient_name
        self.ingredient_quantity = ingredient_quantity