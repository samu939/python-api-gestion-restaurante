from typing import Awaitable
from apps.ingredients.application.dto.create_ingredient_dto import CreateIngredientDto
from apps.ingredients.domain.ingredient import Ingredient
from apps.ingredients.domain.repositories.ingredient_repository import IngredientRepository
from apps.ingredients.domain.value_objects.ingredient_id import IngredientId
from apps.store.application.errors.store_not_found import StoreNotFoundApplicatonError
from apps.store.domain.repositories.store_repository import StoreRepository
from apps.store.domain.value_objects.store_id import StoreId
from apps.ingredients.domain.value_objects.ingredient_name import IngredientName
from apps.ingredients.domain.value_objects.ingredient_quantity import IngredientQuantity
from core.application.events.event_handler import EventHandler
from core.application.services.application_service import ApplicationService
from core.application.results.result_wrapper import Result
from uuid import uuid4

class CreateIngredientApplicationService(ApplicationService[CreateIngredientDto, str]):
    def __init__(self, ingredient_repository: IngredientRepository, store_repository: StoreRepository,event_handler: EventHandler):
        self.ingredient_repository = ingredient_repository
        self.event_handler = event_handler
        self.store_repository = store_repository

    async def execute(self, input: CreateIngredientDto) -> Awaitable[Result[str]]:
        store = await self.store_repository.get_store_by_id(StoreId(input.store_id))
        if store is None:
            return Result[Ingredient].failure(
                error=StoreNotFoundApplicatonError(StoreId(input.store_id))
            ) 
        domain_ingredient = Ingredient(IngredientId(str(uuid4())), IngredientName(input.name), IngredientQuantity(input.quantity), StoreId(input.store_id))
        await self.event_handler.publish_events(domain_ingredient.pull_events())
        ingredient = await self.ingredient_repository.save_ingredient(domain_ingredient)
        return Result[str].success(value="ingrediente guardado") # type: ignore