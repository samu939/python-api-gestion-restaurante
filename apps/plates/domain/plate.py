


from loguru import logger
from apps.ingredients.domain.events.ingredient_changed_store import IngredientChangedStoreEvent
from apps.plates.domain.events.plate_created import PlateCreatedEvent
from apps.ingredients.domain.events.ingredient_quantity_down import IngredientQuantityDownEvent
from apps.ingredients.domain.events.ingredient_quantity_up import IngredientQuantityUpEvent
from apps.plates.domain.value_objects.plate_id import PlateId
from apps.plates.domain.value_objects.plate_name import PlateName
from apps.plates.domain.value_objects.plate_description import PlateDescription
from apps.plates.domain.value_objects.plate_ingredient import PlateIngredient
from apps.ingredients.domain.value_objects.ingredient_quantity import IngredientQuantity
from apps.store.domain.value_objects.store_id import StoreId
from core.domain.aggregates.aggregate import Aggregate
from core.domain.entities.entity import Entity


class Plate (Aggregate[PlateId]):
    def __init__(self, id: PlateId, name: PlateName, plate_description: PlateDescription, ingredients: list[PlateIngredient]) -> None:
        super().__init__(id)
        self.name = name
        self.description = plate_description
        self.ingredients = ingredients
        self.on(PlateCreatedEvent(id, name, plate_description, ingredients))

    
    def validate_state(self) -> None:
        self.id.ensureValidState()
        self.name.ensureValidState()
        self.description.ensureValidState()
        for ingredient in self.ingredients:
            ingredient.ensure_valid_state()