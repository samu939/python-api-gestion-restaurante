
from tkinter import Menu
from typing import Awaitable
from databases import Database

from apps.menus.domain.menu import Menu
from apps.menus.domain.repositories.menu_repository import MenuRepository
from apps.menus.domain.value_objects.menu_id import MenuId
from apps.menus.infraestructure.mappers.menus_mapper import MenuMapper

class DbMenusRepository(MenuRepository):
    def __init__(self, db: Database, menus_mapper: MenuMapper) -> None:
        self.db = db
        self.menus_mapper = menus_mapper
        super().__init__()

    async def get_all_menus(self) -> Awaitable[list[Menu]]:
        from apps.menus.infraestructure.queries.menus_queries import GET_ALL_MENUS
        records = await self.db.fetch_all(query=GET_ALL_MENUS)

        return [self.menus_mapper.from_persistence_to_domain(record) for record in records]
    
    async def get_menu_by_id(self, id: MenuId) -> Awaitable[Menu | None]:
        from apps.menus.infraestructure.queries.menus_queries import GET_MENU_BY_ID
        record = await self.db.fetch_one(query=GET_MENU_BY_ID, values={'id': str(id.value)})
        if (not record):
            return None
        
        return self.menus_mapper.from_persistence_to_domain(record)
    
    async def save_menu(self, menu: Menu) -> Awaitable[None]:
        from apps.menus.infraestructure.queries.menus_queries import INSERT_MENU, INSERT_PLATE_MENU
        res = await self.db.execute(query=INSERT_MENU, values={
            'id': str(menu.id.value),
            'name': menu.name.value
        })

        for plate in menu.plates:
            await self.db.execute(query=INSERT_PLATE_MENU, values={
            'menu_id': str(menu.id.value),
            'plate_id': str(plate.value)
        })
    
    async def update(self, menu: Menu) -> Awaitable[None]:
        from apps.menus.infraestructure.queries.menus_queries import INSERT_PLATE_MENU, UPDATE_MENU, DELETE_MENU_PLATES

        await self.db.execute(query=UPDATE_MENU, values={
            'id': str(menu.id.value),
            'name': menu.name.value
        })
        await self.db.execute(query=DELETE_MENU_PLATES, values={
            'id': str(menu.id.value)
        })

        for plate in menu.plates:
            await self.db.execute(query=INSERT_PLATE_MENU, values={
                'menu_id': str(menu.id.value),
                'plate_id': str(plate.value)
            })
