from apps.menus.domain.value_objects.menu_id import MenuId
from apps.menus.domain.value_objects.menu_name import MenuName
from apps.plates.domain.value_objects.plate_id import PlateId
from apps.plates.domain.value_objects.plate_name import PlateName
from apps.plates.domain.value_objects.plate_description import PlateDescription
from apps.plates.domain.value_objects.plate_ingredient import PlateIngredient
from apps.plates.domain.value_objects.plate_price import PlatePrice
from core.domain.events.domain_event import DomainEvent

class MenuCreatedEvent(DomainEvent):
    def __init__(self, id: MenuId, menu_name: MenuName, menu_plates: list[PlateId]) -> None:
        super().__init__()
        self.id = id
        self.menu_name = menu_name
        self.menu_plates = menu_plates
        