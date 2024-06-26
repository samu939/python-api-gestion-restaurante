
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

    async def save_plate(self, plate: Plate) -> Awaitable[None]:
        from apps.plates.infrastructure.queries.plates_queries import INSERT_NEW_PLATE, INSERT_NEW_PLATE_INGREDIENTS

        res = await self.db.execute(query=INSERT_NEW_PLATE, values={
            'id': plate.id.value,
            'name': plate.name.value,
            'description': plate.description.value,
            'price': plate.price.value
        })

        print(res)

        for ingredient in plate.ingredients:
            await self.db.execute(query=INSERT_NEW_PLATE_INGREDIENTS, values={
                'plate_id': plate.id.value,
                'ingredient_id': str(ingredient.value['ingredient_id'].value),
                'quantity': ingredient.value['quantity'].value
            })
