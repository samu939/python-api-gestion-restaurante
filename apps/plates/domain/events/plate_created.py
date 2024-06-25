from apps.plates.domain.value_objects.plate_id import PlateId
from apps.plates.domain.value_objects.plate_name import PlateName
from apps.plates.domain.value_objects.plate_description import PlateDescription
from apps.plates.domain.value_objects.plate_ingredient import PlateIngredient
from apps.plates.domain.value_objects.plate_price import PlatePrice
from core.domain.events.domain_event import DomainEvent

class PlateCreatedEvent(DomainEvent):
    def __init__(self, id: PlateId, plate_name: PlateName, plate_description: PlateDescription, plate_price: PlatePrice ,plate_ingredients: list[PlateIngredient]) -> None:
        super().__init__()
        self.id = id
        self.plate_name = plate_name
        self.plate_description = plate_description
        self.plate_price = plate_price
        self.plate_ingredients = plate_ingredients
        