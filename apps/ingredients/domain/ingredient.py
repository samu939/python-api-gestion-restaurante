


from apps.ingredients.domain.events.ingredient_created import IngredientCreatedEvent
from apps.ingredients.domain.value_objects.ingredient_id import IngredientId
from apps.ingredients.domain.value_objects.ingredient_name import IngredientName
from apps.ingredients.domain.value_objects.ingredient_quantity import IngredientQuantity
from core.domain.aggregates.aggregate import Aggregate


class Ingredient (Aggregate[IngredientId]):
    def __init__(self, id: IngredientId, name: IngredientName, quantity: IngredientQuantity) -> None:
        super().__init__(id)
        self.name = name
        self.quantity = quantity
        self.on(IngredientCreatedEvent(id, name, quantity))
    
    @property
    def name(self) -> IngredientName:
        return self.name
    
    def validate_state(self) -> None:
        self.id.ensureValidState()
        self.name.ensureValidState()
        self.quantity.ensureValidState()