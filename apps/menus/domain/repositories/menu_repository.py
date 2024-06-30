from abc import abstractmethod
from tkinter import Menu
from typing import Awaitable, Optional

from apps.menus.domain.value_objects.menu_id import MenuId

class MenuRepository:
    @abstractmethod
    def get_menu_by_id(self, id: MenuId) -> Awaitable[Optional[Menu]]:
        pass
    @abstractmethod
    def get_all_menus(self) -> Awaitable[list[Menu]]:
        pass
    @abstractmethod
    def save_menu(self, menu: Menu) -> Awaitable[None]:
        pass
    
