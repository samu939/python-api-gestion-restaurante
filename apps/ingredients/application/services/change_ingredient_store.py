from typing import Awaitable
from apps.ingredients.application.dto.ingredient_change_store_dto import IngredientChangeStoreDto
from apps.ingredients.application.errors.ingredients_not_found import IngredientsNotFoundApplicatonError
from apps.ingredients.domain.ingredient import Ingredient
from apps.ingredients.domain.repositories.ingredient_repository import IngredientRepository
from apps.ingredients.domain.value_objects.ingredient_id import IngredientId
from apps.ingredients.domain.value_objects.ingredient_quantity import IngredientQuantity
from apps.store.domain.value_objects.store_id import StoreId
from core.application.events.event_handler import EventHandler
from core.application.services.application_service import ApplicationService
from core.application.results.result_wrapper import Result
from uuid import uuid4
from loguru import logger

class ChangeIngredientStoreApplicationService(ApplicationService[IngredientChangeStoreDto, Ingredient]):
    def __init__(self, ingredient_repository: IngredientRepository, event_handler: EventHandler):
        self.ingredient_repository = ingredient_repository
        self.event_handler = event_handler

    async def execute(self, input: IngredientChangeStoreDto) -> Awaitable[Result[str]]:
        ingredient = await self.ingredient_repository.get_ingredient_by_id(IngredientId(input.ingredient_id))
        if ingredient is None:
            return Result[Ingredient].failure(
                error=IngredientsNotFoundApplicatonError(input)
            ) # type: ignore
        ingredient.change_store(StoreId(input.store_id))
        await self.event_handler.publish_events(ingredient.pull_events())
        await self.ingredient_repository.save_ingredient(ingredient)
        return Result[Ingredient].success(value=ingredient) # type: ignore