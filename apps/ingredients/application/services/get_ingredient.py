from typing import Awaitable
from apps.ingredients.domain.ingredient import Ingredient
from apps.ingredients.domain.repositories.ingredient_repository import IngredientRepository
from apps.ingredients.domain.value_objects.ingredient_id import IngredientId
from core.application.services.application_service import ApplicationService
from core.application.results.result_wrapper import Result
from ..errors.ingredients_not_found import IngredientsNotFoundApplicatonError

class GetIngredientApplicationService(ApplicationService[IngredientId, Ingredient]):
    def __init__(self, ingredient_repository: IngredientRepository):
        self.ingredient_repository = ingredient_repository

    async def execute(self, input: IngredientId) -> Awaitable[Result[Ingredient]]:
        ingredient = await self.ingredient_repository.get_ingredient_by_id(input)
        if ingredient is None:
            return Result[Ingredient].failure(
                error=IngredientsNotFoundApplicatonError(input)
            ) # type: ignore
        return Result[Ingredient].success(value=ingredient) # type: ignore