

import json
from apps.menus.domain.menu import Menu
from apps.menus.domain.value_objects.menu_id import MenuId
from apps.menus.domain.value_objects.menu_name import MenuName
from apps.plates.domain.value_objects.plate_id import PlateId
from core.application.mappers.mapper import Mapper


class MenuMapper(Mapper[Menu, dict[str, str]]):
    def __init__(self) -> None:
        super().__init__()
    
    def from_domain_to_persistence(self, domain_entity: Menu):
        pass
    
    def from_persistence_to_domain(self, persistence_menu: dict[str, str]) -> Menu:

        plates: list[PlateId] = []

        for plate in json.loads(persistence_menu['plates']):
            plates.append(PlateId(plate['plate_id']))

        return Menu(
            MenuId(persistence_menu['id']),
            MenuName(persistence_menu['name']),
            plates
        )