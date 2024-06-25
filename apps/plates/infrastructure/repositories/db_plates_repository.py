
from typing import Awaitable
from databases import Database

from apps.plates.domain.plate import Plate
from apps.plates.domain.repositories.plates_repository import PlateRepository
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

