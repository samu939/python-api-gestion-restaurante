
from loguru import logger
from apps.plates.domain.events.plate_created import PlateCreatedEvent
from apps.plates.domain.value_objects.plate_id import PlateId
from apps.plates.domain.value_objects.plate_name import PlateName
from apps.plates.domain.value_objects.plate_description import PlateDescription
from apps.plates.domain.value_objects.plate_ingredient import PlateIngredient
from apps.plates.domain.value_objects.plate_price import PlatePrice
from core.domain.aggregates.aggregate import Aggregate


class Plate (Aggregate[PlateId]):
    def __init__(self, id: PlateId, name: PlateName, plate_description: PlateDescription, price: PlatePrice, ingredients: list[PlateIngredient]) -> None:
        super().__init__(id)
        self.name = name
        self.description = plate_description
        self.price = price
        self.ingredients = ingredients
        self.on(PlateCreatedEvent(id, name, plate_description, price, ingredients))

    
    def validate_state(self) -> None:
        self.id.ensureValidState()
        self.name.ensureValidState()
        self.description.ensureValidState()
        self.price.ensureValidState()
        for ingredient in self.ingredients:
            ingredient.ensureValidState()