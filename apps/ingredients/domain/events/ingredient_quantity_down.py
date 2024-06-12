from apps.ingredients.domain.value_objects.ingredient_id import IngredientId
from apps.ingredients.domain.value_objects.ingredient_quantity import IngredientQuantity
from core.domain.events.domain_event import DomainEvent

class IngredientQuantityDownEvent(DomainEvent):
    def __init__(self, ingredient_id: IngredientId, quantity_rested: IngredientQuantity) -> None:
        super().__init__()
        self.ingredient_id = ingredient_id
        self.quantity_rested = quantity_rested
        