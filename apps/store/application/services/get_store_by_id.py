from typing import Awaitable
from apps.ingredients.domain.repositories.ingredient_repository import IngredientRepository
from apps.store.application.dto.get_store_by_id_response_dto import GetStoreByIdResponseDto, StoreIngredient
from apps.store.domain.store import Store
from apps.store.domain.repositories.store_repository import StoreRepository
from apps.store.domain.value_objects.store_id import StoreId
from core.application.services.application_service import ApplicationService
from core.application.results.result_wrapper import Result
from ..errors.store_not_found import StoreNotFoundApplicatonError

class GetStoreApplicationService(ApplicationService[StoreId, GetStoreByIdResponseDto]):
    def __init__(self, store_repository: StoreRepository, ingredient_repository: IngredientRepository):
        self.store_repository = store_repository
        self.ingredient_repository = ingredient_repository

    async def execute(self, input: StoreId) -> Awaitable[Result[GetStoreByIdResponseDto]]:
        store = await self.store_repository.get_store_by_id(input)
        if store is None:
            return Result[GetStoreByIdResponseDto].failure(
                error=StoreNotFoundApplicatonError(input)
            ) # type: ignore
        store_ingredients = await self.ingredient_repository.get_store_ingredients(input)
        ingredients: list[StoreIngredient] = []
        for ing in store_ingredients:
            ingredients.append(StoreIngredient(
                id = ing.id.value,
                name = ing.name.value,
                quantity = ing.quantity.value
            ))
        response = GetStoreByIdResponseDto(
            id=store.id.value,
            name=store.name.value,
            ingredients=ingredients
        )
        return Result[GetStoreByIdResponseDto].success(value=response) # type: ignore
    