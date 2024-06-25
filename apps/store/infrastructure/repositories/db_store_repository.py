


from typing import Awaitable
from uuid import UUID
from databases import Database
from loguru import logger
from apps.ingredients.domain.ingredient import Ingredient
from apps.ingredients.domain.value_objects.ingredient_id import IngredientId
from apps.store.domain.repositories.store_repository import StoreRepository
from apps.store.domain.store import Store
from apps.store.domain.value_objects.store_id import StoreId
from apps.store.infrastructure.mappers.store_mapper import StoreMapper


class DbStoreRepository (StoreRepository):
    def __init__(self, db: Database, store_mapper: StoreMapper) -> None:
        self.db=db
        self.store_mapper = store_mapper
        super().__init__()
        
    async def save_store(self, store: Store) -> Awaitable[None]:
        from apps.store.infrastructure.queries.store_queries import INSERT_STORE
        values = self.store_mapper.from_domain_to_persistence(store)
        await self.db.execute(INSERT_STORE, values= values)
        
    async def get_store_by_id(self, id: StoreId) -> Awaitable[Store | None]:
        from apps.store.infrastructure.queries.store_queries import GET_STORE_BY_ID
        values = {"id": str(id.value)}
        record = await self.db.fetch_one(query=GET_STORE_BY_ID, values=values)

        if not record:
            return None
        
        return self.store_mapper.from_persistence_to_domain(record)
    
    async def get_all_stores(self) -> Awaitable[list[Store]]:
        from apps.store.infrastructure.queries.store_queries import GET_ALL_STORES
        records = await self.db.fetch_all(query=GET_ALL_STORES)
        return [self.store_mapper.from_persistence_to_domain(record) for record in records]
    