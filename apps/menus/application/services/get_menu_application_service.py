
from typing import Awaitable
from apps.menus.application.errors.menu_not_found import MenuNotFoundApplicatonError
from apps.menus.domain.menu import Menu
from apps.menus.domain.repositories.menu_repository import MenuRepository
from apps.menus.domain.value_objects.menu_id import MenuId
from apps.menus.infraestructure.responses.menus_responses import GetMenuWithPlatesResponse, MenuPlates
from apps.plates.application.errors.plate_not_found import PlateNotFoundApplicatonError
from apps.plates.domain.plate import Plate
from apps.plates.domain.repositories.plates_repository import PlateRepository
from core.application.results.result_wrapper import Result
from core.application.services.application_service import ApplicationService


class GetMenuByIdApplicationService(ApplicationService[MenuId, GetMenuWithPlatesResponse]):
    def __init__(self, menus_repository: MenuRepository, plates_repository: PlateRepository) -> MenuId:
        self.menus_repository = menus_repository
        self.plates_repository = plates_repository

    async def execute(self, input: MenuId) -> Awaitable[Result[GetMenuWithPlatesResponse]]:
        menu: Menu = await self.menus_repository.get_menu_by_id(input)

        if not menu:
            return Result[Menu].failure(
                error=MenuNotFoundApplicatonError(input))
        
        domain_plates: list[Plate] = []

        for plate in menu.plates:
            domain_plate = await self.plates_repository.get_plate_by_id(plate)
            if domain_plate is None:
                return Result[Plate].failure(
                    error=PlateNotFoundApplicatonError(plate))
            domain_plates.append(domain_plate) 
        
        plates: list[MenuPlates] = []
        
        for plate in domain_plates:
            plates.append(MenuPlates(id=plate.id.value, name=plate.name.value, price=plate.price.value))
        
        return Result[GetMenuWithPlatesResponse].success(value=GetMenuWithPlatesResponse(id=menu.id.value, name=menu.name.value, plates=plates))