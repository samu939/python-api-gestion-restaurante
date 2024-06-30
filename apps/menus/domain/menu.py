
from apps.menus.domain.value_objects.menu_id import MenuId
from apps.menus.domain.value_objects.menu_name import MenuName
from apps.plates.domain.value_objects.plate_id import PlateId


class Menu:

    def __init__(self, id: MenuId, name: MenuName, plates: list[PlateId]) -> None:
        self.id = id
        self.name = name
        self.plates = plates