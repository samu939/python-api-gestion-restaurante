from typing import Awaitable
from apps.store.domain.store import Store
from apps.store.domain.repositories.store_repository import StoreRepository
from apps.store.domain.value_objects.store_id import StoreId
from core.application.services.application_service import ApplicationService
from core.application.results.result_wrapper import Result
from ..errors.store_not_found import StoreNotFoundApplicatonError

class GetStoreApplicationService(ApplicationService[StoreId, Store]):
    def __init__(self, store_repository: StoreRepository):
        self.store_repository = store_repository

    async def execute(self, input: StoreId) -> Awaitable[Result[Store]]:
        store = await self.store_repository.get_store_by_id(input)
        if store is None:
            return Result[Store].failure(
                error=StoreNotFoundApplicatonError(input)
            ) # type: ignore
        store_ingredients = await self.store_repository.get_store_ingredients(input)

        store.add_ingredients(store_ingredients)
        return Result[Store].success(value=store) # type: ignore
    