from typing import Awaitable
from apps.store.application.dto.create_store_dto import CreateStoreDto
from apps.store.domain.repositories.store_repository import StoreRepository
from apps.store.domain.store import Store
from apps.store.domain.value_objects.store_id import StoreId
from apps.store.domain.value_objects.store_name import StoreName
from core.application.events.event_handler import EventHandler
from core.application.services.application_service import ApplicationService
from core.application.results.result_wrapper import Result
from uuid import uuid4

class CreateStoreApplicationService(ApplicationService[CreateStoreDto, str]):
    def __init__(self, store_repository: StoreRepository, event_handler: EventHandler):
        self.store_repository = store_repository
        self.event_handler = event_handler

    async def execute(self, input: CreateStoreDto) -> Awaitable[Result[str]]:
        store = Store(StoreId(str(uuid4())), StoreName(input.name), [])
        await self.event_handler.publish_events(store.pull_events())
        store = await self.store_repository.save_store(store)
        return Result[str].success(value="almacen guardado") # type: ignore