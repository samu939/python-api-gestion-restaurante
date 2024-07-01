from typing import Awaitable
from apps.ingredients.domain.value_objects.ingredient_id import IngredientId
<<<<<<< HEAD
from apps.plates.application.dtos.modify_plate_dto import ModifyPlateDto
=======
>>>>>>> 9d6328e (modificar platos calidad)
from apps.plates.application.errors.plate_not_found import PlateNotFoundApplicatonError
from apps.plates.domain.plate import Plate
from apps.plates.domain.repositories.plates_repository import PlateRepository
from apps.plates.domain.value_objects.ingredient_for_plate_quantity import IngredientForPlateQuantity
from apps.plates.domain.value_objects.plate_id import PlateId
from apps.plates.domain.value_objects.plate_ingredient import PlateIngredient
from apps.plates.domain.value_objects.plate_price import PlatePrice
<<<<<<< HEAD
=======
from apps.plates.infrastructure.dtos.modify_plate_dto import ModifyPlateDto
>>>>>>> 9d6328e (modificar platos calidad)
from core.application.events.event_handler import EventHandler
from core.application.results.result_wrapper import Result
from core.application.services.application_service import ApplicationService


class ModifyplateApplicationService(ApplicationService[ModifyPlateDto, str]):
    def __init__(self, plates_repository: PlateRepository, event_handler: EventHandler) -> None:
        self.plates_repository = plates_repository
        self.event_handler = event_handler

    async def execute(self, input: ModifyPlateDto) -> Awaitable[Result[str]]:

        plate = await self.plates_repository.get_plate_by_id(PlateId(input.id))
        if plate is None:
            return Result[str].failure(
                error=PlateNotFoundApplicatonError(PlateId(input.id))
            )

        domain_plate_ingredients = []

        for ingredient in input.ingredients:
            domain_plate_ingredients.append(PlateIngredient({
                'ingredient_id': IngredientId(ingredient.id),
                'quantity': IngredientForPlateQuantity(ingredient.quantity)
            }))

        modified_plate = Plate(plate.id, plate.name, plate.description,
                             PlatePrice(input.price), domain_plate_ingredients)
        await self.event_handler.publish_events(modified_plate.pull_events())
        await self.plates_repository.update(modified_plate)
        return Result[str].success(value="Plato guardado")
