
from typing import Awaitable
from databases import Database

from apps.plates.domain.plate import Plate
from apps.plates.domain.repositories.plates_repository import PlateRepository
from apps.plates.domain.value_objects.plate_id import PlateId
from apps.plates.infrastructure.mappers.plates_mapper import PlateMapper



class DbPlatesRepository(PlateRepository):
    def __init__(self, db: Database, plates_mapper: PlateMapper) -> None:
        self.db = db
        self.plates_mapper = plates_mapper
        super().__init__()

    async def get_all_plates(self) -> Awaitable[list[Plate]]:
        from apps.plates.infrastructure.queries.plates_queries import GET_ALL_PLATES
        records = await self.db.fetch_all(query=GET_ALL_PLATES)

        return [self.plates_mapper.from_persistence_to_domain(record) for record in records]
    
    async def get_plate_by_id(self, id: PlateId) -> Awaitable[Plate | None]:
        from apps.plates.infrastructure.queries.plates_queries import GET_PLATE_BY_ID
        
        record = await self.db.fetch_one(query=GET_PLATE_BY_ID, values={'id': str(id.value)})

        return self.plates_mapper.from_persistence_to_domain(record)

