from typing import Awaitable
from apps.ingredients.domain.value_objects.ingredient_id import IngredientId
from apps.menus.application.dtos.modify_menu_dto import ModifyMenuDto
from apps.menus.application.errors.menu_not_found import MenuNotFoundApplicatonError
from apps.menus.domain.menu import Menu
from apps.menus.domain.repositories.menu_repository import MenuRepository
from apps.menus.domain.value_objects.menu_id import MenuId
from apps.menus.domain.value_objects.menu_name import MenuName
from apps.plates.application.errors.plate_not_found import PlateNotFoundApplicatonError
from apps.plates.domain.plate import Plate
from apps.plates.domain.repositories.plates_repository import PlateRepository
from apps.plates.domain.value_objects.ingredient_for_plate_quantity import IngredientForPlateQuantity
from apps.plates.domain.value_objects.plate_id import PlateId
from apps.plates.domain.value_objects.plate_ingredient import PlateIngredient
from apps.plates.domain.value_objects.plate_price import PlatePrice
from core.application.events.event_handler import EventHandler
from core.application.results.result_wrapper import Result
from core.application.services.application_service import ApplicationService


class ModifyMenuApplicationService(ApplicationService[ModifyMenuDto, str]):
    def __init__(self, menus_repository: MenuRepository, plates_repository: PlateRepository, event_handler: EventHandler) -> None:
        self.menus_repository = menus_repository
        self.event_handler = event_handler
        self.plates_repository = plates_repository

    async def execute(self, input: ModifyMenuDto) -> Awaitable[Result[str]]:

        menu: Menu = await self.menus_repository.get_menu_by_id(MenuId(input.id))
        if menu is None:
            return Result[str].failure(error=MenuNotFoundApplicatonError(PlateId(input.id)))

        domain_menu_plates = []
        
        for plate in input.plates:
            domain_plate = await self.plates_repository.get_plate_by_id(PlateId(plate))
            if domain_plate is None:
                return Result[Plate].failure(
                    error=PlateNotFoundApplicatonError(plate))
            domain_menu_plates.append(PlateId(plate))


        modified_menu = Menu(id=menu.id, name=MenuName(input.name), plates=domain_menu_plates)
        await self.event_handler.publish_events(modified_menu.pull_events())
        await self.menus_repository.update(modified_menu)
        return Result[str].success(value="Menú guardado")
