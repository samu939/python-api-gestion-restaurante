
from tkinter import Menu
from typing import Awaitable
from apps.menus.domain.repositories.menu_repository import MenuRepository
from apps.plates.domain.plate import Plate
from apps.plates.domain.repositories.plates_repository import PlateRepository
from core.application.results.result_wrapper import Result
from core.application.services.application_service import ApplicationService


class GetAllMenusApplicationService(ApplicationService[None, list[Menu]]):
    def __init__(self, menus_repository: MenuRepository) -> None:
        self.menus_repository = menus_repository

    async def execute(self, input: None) -> Awaitable[Result[list[Menu]]]:
        menus = await self.menus_repository.get_all_menus()
        return Result[list[Menu]].success(value=menus)