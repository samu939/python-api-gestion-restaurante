from typing import Awaitable
from uuid import uuid4
from apps.ingredients.application.errors.ingredients_not_found import IngredientsNotFoundApplicatonError
from apps.ingredients.domain.repositories.ingredient_repository import IngredientRepository
from apps.ingredients.domain.value_objects.ingredient_id import IngredientId
from apps.plates.application.dtos.create_plate_dto import CreatePlateDto
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


class CreatePlateApplicationService(ApplicationService[CreatePlateDto, str]):
    def __init__(self, plates_repository: PlateRepository, ingredients_repository: IngredientRepository, event_handler: EventHandler) -> None:
        self.plates_repository = plates_repository
        self.event_handler = event_handler
        self.ingredients_repository = ingredients_repository

    async def execute(self, input: CreatePlateDto) -> Awaitable[Result[str]]:

        domain_plate_ingredients = []

        for ingredient in input.ingredients:
            domain_ingredient = await self.ingredients_repository.get_ingredient_by_id(IngredientId(ingredient.id))
            if domain_ingredient is None:
                return Result[str].failure(IngredientsNotFoundApplicatonError(IngredientId(ingredient.id)))

            domain_plate_ingredients.append(PlateIngredient({
                'ingredient_id': IngredientId(ingredient.id),
                'quantity': IngredientForPlateQuantity(ingredient.quantity)
            }))

        domain_plate = Plate(PlateId(str(uuid4())), PlateName(input.name), PlateDescription(input.description),
                             PlatePrice(input.price), domain_plate_ingredients)
        await self.event_handler.publish_events(domain_plate.pull_events())
        await self.plates_repository.save_plate(domain_plate)
        return Result[str].success(value="Plato guardado") # type: ignore
