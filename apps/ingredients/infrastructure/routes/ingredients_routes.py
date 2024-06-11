from uuid import UUID
from databases import Database
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from apps.auth.application.dto.login_dto import loginDto
from apps.auth.application.services.login_service import loginService
from apps.auth.infraestructure.dependecies.auth_dependecies import get_current_active_user
from apps.auth.infraestructure.jwt.jwt_generator import jwtGenerator
from apps.ingredients.application.services.get_ingredient import GetIngredientApplicationService
from apps.ingredients.domain.ingredient import Ingredient
from apps.ingredients.domain.value_objects.ingredient_id import IngredientId
from apps.ingredients.infrastructure.db_entity.ingredient_in_db import IngredientInDB
from apps.ingredients.infrastructure.mappers.ingredient_mapper import IngredientMapper
from apps.ingredients.infrastructure.repositories.db_ingredients_repository import DbIngredientsRepository
from apps.ingredients.infrastructure.responses.ingredients_responses import GetIngredientResponse
from apps.user.infrastructure.db_entity.user_in_db import UserInDB
from core.application.decorators.exception_decorator import ExceptionDecorator
from db.db_dependencies import get_database

ingredient_router = APIRouter(
    prefix="/ingredient",
    tags=["ingredient"],
    responses={404: {"description": "Not found"}},
)

@ingredient_router.post("/get/{id}", response_model=GetIngredientResponse, name="ingredient:getById")
async def getIngredientById(
    id: UUID,
    db: Database = Depends(get_database),
    current_user: UserInDB = Depends(get_current_active_user),
):

    service = ExceptionDecorator(GetIngredientApplicationService(ingredient_repository= DbIngredientsRepository(db,IngredientMapper())))
    
    return (await service.execute(IngredientId(id))).unwrap()