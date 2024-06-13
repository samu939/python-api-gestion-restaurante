


from loguru import logger
from apps.ingredients.domain.events.ingredient_created import IngredientCreatedEvent
from apps.ingredients.domain.events.ingredient_quantity_down import IngredientQuantityDownEvent
from apps.ingredients.domain.events.ingredient_quantity_up import IngredientQuantityUpEvent
from apps.ingredients.domain.value_objects.ingredient_id import IngredientId
from apps.ingredients.domain.value_objects.ingredient_name import IngredientName
from apps.ingredients.domain.value_objects.ingredient_quantity import IngredientQuantity
from core.domain.aggregates.aggregate import Aggregate
from core.domain.entities.entity import Entity


class Ingredient (Aggregate[IngredientId]):
    def __init__(self, id: IngredientId, name: IngredientName, quantity: IngredientQuantity) -> None:
        super().__init__(id)
        self.name = name
        self.quantity = quantity
        self.on(IngredientCreatedEvent(id, name, quantity))

    
    def validate_state(self) -> None:
        self.id.ensureValidState()
        self.name.ensureValidState()
        self.quantity.ensureValidState()
        
    def add_quantity(self, quantity: IngredientQuantity) -> None:
        ingredient_quantity_up_event = IngredientQuantityUpEvent(self.id, quantity)
        before_quantity = self.quantity.value
        added_quantity = quantity.value
        new_quantity = before_quantity + added_quantity
        self.quantity = IngredientQuantity(new_quantity)
        self.on(ingredient_quantity_up_event)
        
    def rest_quantity(self, quantity: IngredientQuantity) -> None:
        ingredient_quantity_down_event = IngredientQuantityDownEvent(self.id, quantity)
        logger.info(quantity.value)
        before_quantity = self.quantity.value
        rest_quantity = quantity.value
        new_quantity = before_quantity - rest_quantity
        self.quantity = IngredientQuantity(new_quantity)
        self.on(ingredient_quantity_down_event)