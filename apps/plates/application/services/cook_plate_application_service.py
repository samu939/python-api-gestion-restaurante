from typing import Awaitable
from uuid import uuid4
from apps.ingredients.domain.ingredient import Ingredient
from apps.ingredients.domain.repositories.ingredient_repository import IngredientRepository
from apps.ingredients.domain.value_objects.ingredient_quantity import IngredientQuantity
from apps.plates.application.dtos.cook_plate_dto import CookPlateDto
from apps.plates.application.errors.plate_not_found import PlateNotFoundApplicatonError
from apps.plates.domain.plate import Plate
from apps.plates.domain.repositories.plates_repository import PlateRepository
from core.application.events.event_handler import EventHandler
from core.application.results.result_wrapper import Result
from core.application.services.application_service import ApplicationService
from core.domain.exceptions.domain_exception import DomainException


class CookPlateApplicationService(ApplicationService[CookPlateDto, str]):
    def __init__(self, plates_repository: PlateRepository, ingredients_repository: IngredientRepository, event_handler: EventHandler) -> None:
        self.plates_repository = plates_repository
        self.ingredients_repository = ingredients_repository
        self.event_handler = event_handler

    async def execute(self, input: CookPlateDto) -> Awaitable[Result[str]]:

        try:
            plate = await self.plates_repository.get_plate_by_id(input.plate_id)
        
            if not plate:
                raise PlateNotFoundApplicatonError

            plate_ingredients: list[Ingredient] = []
            
            for ingredient in plate.ingredients:
                plate_ingredients.append({
                    'ingredient': await self.ingredients_repository.get_ingredient_by_id(ingredient.value['ingredient_id']),
                    'quantity': IngredientQuantity(ingredient.value['quantity'].value * input.quantity.value)
                })    
            
            for item in plate_ingredients:
                item['ingredient'].rest_quantity(item['quantity'])
                await self.ingredients_repository.save_ingredient(item['ingredient'])
                
            
            return Result[str].success(value="Platos cocinandose") # type: ignore
        
        except DomainException as error:
            return Result[DomainException].failure(error=error)