from typing import Awaitable
from databases import Database
from apps.ingredients.domain.ingredient import Ingredient
from apps.ingredients.domain.repositories.ingredient_repository import IngredientRepository
from apps.ingredients.domain.value_objects.ingredient_id import IngredientId
from apps.ingredients.infrastructure.mappers.ingredient_mapper import IngredientMapper
from apps.store.domain.value_objects.store_id import StoreId


class DbIngredientsRepository (IngredientRepository):
    def __init__(self, db: Database, ingredient_mapper: IngredientMapper) -> None:
        self.db=db
        self.ingredientMapper = ingredient_mapper
        super().__init__()
        
    async def get_ingredient_by_id(self, id: IngredientId) -> Awaitable[Ingredient | None]:
        from apps.ingredients.infrastructure.queries.ingredients_queries import GET_INGREDIENT_BY_ID
        values = {"id": str(id.value)}
        print(values)
        record = await self.db.fetch_one(query=GET_INGREDIENT_BY_ID, values=values)
        if not record:
            return None
        
        return self.ingredientMapper.from_persistence_to_domain(record)
    
    async def save_ingredient(self, ingredient: Ingredient) -> Awaitable[None]:
        from apps.ingredients.infrastructure.queries.ingredients_queries import INSERT_INGREDIENT, INSERT_INGREDIENT_INTO_STORE, SEARCH_BY_NAME, SEARCH_ING_STORE_RELATION, UPDATE_QUANTITY
        values = self.ingredientMapper.from_domain_to_persistence(ingredient)

        ingredient_in_db = await self.db.fetch_one(query=SEARCH_BY_NAME, values={'name': values['name']})

        if (not ingredient_in_db):
            await self.db.execute(query=INSERT_INGREDIENT, values= {
                'id': values['id'],
                'name': values['name']
            })
            await self.db.execute(query=INSERT_INGREDIENT_INTO_STORE, values={
                'ingredient_id': values['id'],
                'store_id': values['store_id'],
                'quantity': values['quantity']
            })

            return
        
        ingredient_store_relation_in_db = await self.db.fetch_one(SEARCH_ING_STORE_RELATION, values={
            'fk_ingredient': ingredient_in_db.id,
            'fk_store': values['store_id'],
        })

        if (ingredient_store_relation_in_db):
            await self.db.execute(query=UPDATE_QUANTITY, values={
                'id': ingredient.id.value,
                'quantity': values['quantity']
            })
            return

        await self.db.execute(query=INSERT_INGREDIENT_INTO_STORE, values={
            'ingredient_id': ingredient_in_db.id,
            'store_id': values['store_id'],
            'quantity': values['quantity']
        })
        
    async def get_all_ingredients(self) -> Awaitable[list[Ingredient]]:
        from apps.ingredients.infrastructure.queries.ingredients_queries import GET_ALL_INGREDIENTS
        records = await self.db.fetch_all(query=GET_ALL_INGREDIENTS)
        return [self.ingredientMapper.from_persistence_to_domain(record) for record in records]
        
    async def get_store_ingredients(self, id: StoreId) -> Awaitable[list[Ingredient]]:
        from apps.ingredients.infrastructure.queries.ingredients_queries import GET_STORE_INGREDIENTS
        values = {"id": str(id.value)}
        record = await self.db.fetch_all(query=GET_STORE_INGREDIENTS, values=values)
        return [self.ingredientMapper.from_persistence_to_domain(record) for record in record]
        
    