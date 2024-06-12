from apps.ingredients.domain.value_objects.ingredient_id import IngredientId
from apps.ingredients.domain.value_objects.ingredient_quantity import IngredientQuantity
from core.domain.events.domain_event import DomainEvent

class IngredientQuantityUpEvent(DomainEvent):
    def __init__(self, ingredient_id: IngredientId, quantity_added: IngredientQuantity) -> None:
        super().__init__()
        self.ingredient_id = ingredient_id
        self.quantity_added = quantity_added
        