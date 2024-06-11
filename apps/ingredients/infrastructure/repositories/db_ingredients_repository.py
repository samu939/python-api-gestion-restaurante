


from typing import Awaitable
from databases import Database
from apps.ingredients.domain.ingredient import Ingredient
from apps.ingredients.domain.repositories.ingredient_repository import IngredientRepository
from apps.ingredients.domain.value_objects.ingredient_id import IngredientId
from apps.ingredients.infrastructure.mappers.ingredient_mapper import IngredientMapper


class DbIngredientsRepository (IngredientRepository):
    def __init__(self, db: Database, ingredient_mapper: IngredientMapper) -> None:
        self.db=db
        self.ingredientMapper = ingredient_mapper
        super().__init__()
        
    async def get_ingredient_by_id(self, id: IngredientId) -> Awaitable[Ingredient | None]:
        from apps.ingredients.infrastructure.queries.ingredients_queries import GET_INGREDIENT_BY_ID
        values = {"id": id.value}
        record = await self.db.fetch_one(query=GET_INGREDIENT_BY_ID, values=values)

        if not record:
            return None
        
        return self.ingredientMapper.from_persistence_to_domain(record)
    