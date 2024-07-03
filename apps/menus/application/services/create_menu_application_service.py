from typing import Awaitable
from uuid import uuid4
from apps.ingredients.domain.value_objects.ingredient_id import IngredientId
from apps.menus.application.dtos.create_menu_dto import CreateMenuDto
from apps.menus.domain.menu import Menu
from apps.menus.domain.repositories.menu_repository import MenuRepository
from apps.menus.domain.value_objects.menu_id import MenuId
from apps.menus.domain.value_objects.menu_name import MenuName
from apps.plates.application.errors.plate_not_found import PlateNotFoundApplicatonError
from apps.plates.domain.plate import Plate
from apps.plates.domain.repositories.plates_repository import PlateRepository
from apps.plates.domain.value_objects.ingredient_for_plate_quantity import IngredientForPlateQuantity
from apps.plates.domain.value_objects.plate_description import PlateDescription
from apps.plates.domain.value_objects.plate_id import PlateId
from apps.plates.domain.value_objects.plate_ingredient import PlateIngredient
from apps.plates.domain.value_objects.plate_name import PlateName
from apps.plates.domain.value_objects.plate_price import PlatePrice
from core.application.events.event_handler import EventHandler
from core.application.results.result_wrapper import Result
from core.application.services.application_service import ApplicationService


class CreateMenuApplicationService(ApplicationService[CreateMenuDto, str]):
    def __init__(self, menu_repository: MenuRepository, plates_repository: PlateRepository, event_handler: EventHandler) -> None:
        self.menu_repository = menu_repository
        self.event_handler = event_handler
        self.plates_repository = plates_repository

    async def execute(self, input: CreateMenuDto) -> Awaitable[Result[str]]:

        plates_id: list[PlateId] = []

        for plate in input.plates:
            domain_plate = await self.plates_repository.get_plate_by_id(PlateId(plate))
            if domain_plate is None:
                return Result[str].failure(error=PlateNotFoundApplicatonError(PlateId(plate)))
            plates_id.append(PlateId(plate))

        domain_menu = Menu(id=MenuId(str(uuid4())), name=MenuName(input.name), plates=plates_id)

        await self.event_handler.publish_events(domain_menu.pull_events())
        await self.menu_repository.save_menu(domain_menu)
        return Result[str].success(value="Menú guardado") # type: ignore
