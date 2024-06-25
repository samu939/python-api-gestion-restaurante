from apps.plates.domain.value_objects.plate_id import PlateId
from apps.plates.domain.value_objects.plate_name import PlateName
from apps.plates.domain.value_objects.plate_description import PlateDescription
from apps.plates.domain.value_objects.plate_ingredient import PlateIngredient
from core.domain.events.domain_event import DomainEvent

class PlateCreatedEvent(DomainEvent):
    def __init__(self, id: PlateId, name: PlateName, description: PlateDescription, ingredients: list[PlateIngredient]) -> None:
        super().__init__()
        self.id = id
        self.name = name
        self.description = description
        self.ingredients = ingredients
        