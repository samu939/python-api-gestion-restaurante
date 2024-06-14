from typing import Awaitable
from apps.ingredients.domain.ingredient import Ingredient
from apps.ingredients.domain.repositories.ingredient_repository import IngredientRepository
from core.application.services.application_service import ApplicationService
from core.application.results.result_wrapper import Result
from ..errors.ingredients_not_found import IngredientsNotFoundApplicatonError

class GetAllIngredientsApplicationService(ApplicationService[None, list[Ingredient]]):
    def __init__(self, ingredient_repository: IngredientRepository):
        self.ingredient_repository = ingredient_repository

    async def execute(self, input: None) -> Awaitable[Result[list[Ingredient]]]:
        ingredients = await self.ingredient_repository.get_all_ingredients()
        return Result[list[Ingredient]].success(value=ingredients) # type: ignore