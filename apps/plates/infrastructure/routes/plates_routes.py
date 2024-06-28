from uuid import UUID
from databases import Database
from fastapi import APIRouter, Depends

from apps.auth.infraestructure.dependecies.auth_dependecies import get_current_active_user
from apps.plates.application.services.cook_plate_application_service import CookPlateApplicationService
from apps.plates.domain.value_objects.plate_quantity import PlateQuantity
from apps.plates.infrastructure.dtos.create_plate_dto import CreatePlateDto
from apps.ingredients.infrastructure.mappers.ingredient_mapper import IngredientMapper
from apps.ingredients.infrastructure.repositories.db_ingredients_repository import DbIngredientsRepository
from apps.plates.application.services.get_plate_by_id_application_service import GetPlateByIdApplicationService
from apps.plates.application.services.create_plate_application_service import CreatePlateApplicationService
from apps.plates.application.services.get_all_plates_application_service import GetAllPlatesApplicationService
from apps.plates.domain.value_objects.plate_id import PlateId
from apps.plates.infrastructure.dtos.cook_plate_dto import CookPlateDto
from apps.plates.infrastructure.entries.create_plate_entry import CookPlateEntry, CreatePlateEntry
from apps.plates.infrastructure.mappers.plates_mapper import PlateMapper
from apps.plates.infrastructure.repositories.db_plates_repository import DbPlatesRepository
from apps.plates.infrastructure.responses.plates_responses import GetPlatesIngredientResponse, SavePlateResponse
from apps.plates.infrastructure.responses.plates_responses import GetAllPlatesResponse, GetPlateResponse
from apps.user.infrastructure.db_entity.user_in_db import UserInDB
from core.application.decorators.exception_decorator import ExceptionDecorator
from core.infrastructure.events.event_handler_native import NativeEventHandler
from db.db_dependencies import get_database


plates_router = APIRouter(
    prefix="/plates",
    tags=["plate"],
    responses={404: {"description": "Not found"}},
)

@plates_router.get("/getall", response_model=GetAllPlatesResponse, name="plate:getAll")
async def getPlates(
    db: Database = Depends(get_database),
    current_user: UserInDB = Depends(get_current_active_user)
):
    
    service = ExceptionDecorator(GetAllPlatesApplicationService(plates_repository= DbPlatesRepository(db, PlateMapper())))
    response = (await service.execute(None)).unwrap()
    plates: list[GetPlateResponse] = []
    for plate in response:
        plates.append(GetPlateResponse(id=plate.id.value, name=plate.name.value, description=plate.description.value,
                                       price=plate.price.value, 
                                       ingredients=[
                                           GetPlatesIngredientResponse(id=ingredient.value['ingredient_id'].value, 
                                            quantity=ingredient.value['quantity'].value) for ingredient in plate.ingredients]))
    
    return GetAllPlatesResponse(plates=plates)

@plates_router.get("get/{id}", response_model=GetPlateResponse, name="plate:getById")
async def getPlateById(
    id: UUID,
    db: Database = Depends(get_database),
    current_user: UserInDB = Depends(get_current_active_user)
):
    service = ExceptionDecorator(GetPlateByIdApplicationService(plates_repository= DbPlatesRepository(db, PlateMapper())))
    response = (await service.execute(PlateId(id))).unwrap()
    return GetPlateResponse(id=response.id.value, name=response.name.value, description=response.description.value,
                            price=response.price.value, ingredients=[
                                           GetPlatesIngredientResponse(id=ingredient.value['ingredient_id'].value, 
                                            quantity=ingredient.value['quantity'].value) for ingredient in response.ingredients])

@plates_router.post("/create", response_model=SavePlateResponse, name="plate:create")
async def createPlate(
    new_plate: CreatePlateEntry,
    db: Database = Depends(get_database),
    current_user: UserInDB = Depends(get_current_active_user)
):
    event_handler = NativeEventHandler()
    print(new_plate)
    plate = CreatePlateDto(**new_plate.dict())
    service = ExceptionDecorator(CreatePlateApplicationService(plates_repository= DbPlatesRepository(db, PlateMapper()), event_handler=event_handler))

    return SavePlateResponse(response=((await service.execute(plate)).unwrap()))

@plates_router.post("/cook", response_model=SavePlateResponse, name="plate:cook")
async def cookPlate(
    plate_to_cook: CookPlateEntry,
    db: Database = Depends(get_database),
    current_user: UserInDB = Depends(get_current_active_user)
):
    
    event_handler = NativeEventHandler()
    print(plate_to_cook)
    plate = CookPlateDto(plate_id=PlateId(plate_to_cook.plate_id), quantity=PlateQuantity(plate_to_cook.quantity))
    service = ExceptionDecorator(CookPlateApplicationService(plates_repository= DbPlatesRepository(db, PlateMapper()), ingredients_repository= DbIngredientsRepository(db, IngredientMapper()),event_handler=event_handler))

    return SavePlateResponse(response=((await service.execute(plate)).unwrap()))