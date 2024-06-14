from typing import Awaitable
from apps.ingredients.domain.repositories.ingredient_repository import IngredientRepository
from apps.store.application.dto.get_store_by_id_response_dto import GetStoreByIdResponseDto, StoreIngredient
from apps.store.domain.store import Store
from apps.store.domain.repositories.store_repository import StoreRepository
from apps.store.domain.value_objects.store_id import StoreId
from core.application.services.application_service import ApplicationService
from core.application.results.result_wrapper import Result
from ..errors.store_not_found import StoreNotFoundApplicatonError

class GetAllStoresApplicationService(ApplicationService[None, list[Store]]):
    def __init__(self, store_repository: StoreRepository):
        self.store_repository = store_repository

    async def execute(self, input: None) -> Awaitable[Result[list[Store]]]:
        stores = await self.store_repository.get_all_stores()

        return Result[list[Store]].success(value=stores) # type: ignore
    