from typing import Awaitable
from apps.ingredients.application.dto.create_ingredient_dto import CreateIngredientDto
from apps.ingredients.application.dto.modify_ingredient_quantity_dto import ModifyIngredientQuantityDto
from apps.ingredients.application.errors.ingredients_not_found import IngredientsNotFoundApplicatonError
from apps.ingredients.domain.ingredient import Ingredient
from apps.ingredients.domain.repositories.ingredient_repository import IngredientRepository
from apps.ingredients.domain.value_objects.ingredient_id import IngredientId
from apps.ingredients.domain.value_objects.ingredient_name import IngredientName
from apps.ingredients.domain.value_objects.ingredient_quantity import IngredientQuantity
from core.application.events.event_handler import EventHandler
from core.application.services.application_service import ApplicationService
from core.application.results.result_wrapper import Result
from uuid import uuid4
from loguru import logger

class EgressIngredientApplicationService(ApplicationService[ModifyIngredientQuantityDto, Ingredient]):
    def __init__(self, ingredient_repository: IngredientRepository, event_handler: EventHandler):
        self.ingredient_repository = ingredient_repository
        self.event_handler = event_handler

    async def execute(self, input: ModifyIngredientQuantityDto) -> Awaitable[Result[str]]:
        ingredient = await self.ingredient_repository.get_ingredient_by_id(IngredientId(input.ingredient_id))
        if ingredient is None:
            return Result[Ingredient].failure(
                error=IngredientsNotFoundApplicatonError(input)
            ) # type: ignore
        ingredient.rest_quantity(IngredientQuantity(input.quantity))
        self.event_handler.publish_events(ingredient.pull_events())
        await self.ingredient_repository.save_ingredient(ingredient)
        return Result[Ingredient].success(value=ingredient) # type: ignore