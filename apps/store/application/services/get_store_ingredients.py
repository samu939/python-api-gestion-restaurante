from typing import Awaitable
from apps.ingredients.domain.ingredient import Ingredient
from apps.ingredients.domain.repositories.ingredient_repository import IngredientRepository
from apps.store.domain.value_objects.store_id import StoreId
from core.application.services.application_service import ApplicationService
from core.application.results.result_wrapper import Result

class GetStoresIngredientsApplicationService(ApplicationService[StoreId, list[Ingredient]]):
    def __init__(self, ingredient_repository: IngredientRepository):
        self.ingredient_repository = ingredient_repository

    async def execute(self, input: StoreId) -> Awaitable[Result[list[Ingredient]]]:
        ingredients = await self.ingredient_repository.get_store_ingredients(input)
        return Result[list[Ingredient]].success(value=ingredients) # type: ignore