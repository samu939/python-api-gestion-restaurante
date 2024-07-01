
from apps.menus.domain.events.menu_created import MenuCreatedEvent
from apps.menus.domain.value_objects.menu_id import MenuId
from apps.menus.domain.value_objects.menu_name import MenuName
from apps.plates.domain.events.plate_created import PlateCreatedEvent
from apps.plates.domain.value_objects.plate_id import PlateId
from core.domain.aggregates.aggregate import Aggregate


class Menu(Aggregate[MenuId]):

    def __init__(self, id: MenuId, name: MenuName, plates: list[PlateId]) -> None:
        super().__init__(id)
        self.name = name
        self.plates = plates
        self.on(MenuCreatedEvent(id, name, plates))
    
    def validate_state(self) -> None:
        self.id.ensureValidState()
        self.name.ensureValidState()
        for plate in self.plates:
            plate.ensureValidState()
