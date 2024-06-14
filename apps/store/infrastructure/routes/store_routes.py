from uuid import UUID
from databases import Database
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from apps.auth.application.dto.login_dto import loginDto
from apps.auth.application.services.login_service import loginService
from apps.auth.infraestructure.dependecies.auth_dependecies import get_current_active_user
from apps.auth.infraestructure.jwt.jwt_generator import jwtGenerator
from apps.ingredients.infrastructure.mappers.ingredient_mapper import IngredientMapper
from apps.ingredients.infrastructure.repositories.db_ingredients_repository import DbIngredientsRepository
from apps.store.application.dto.create_store_dto import CreateStoreDto
from apps.store.application.dto.get_store_by_id_response_dto import GetStoreByIdResponseDto
from apps.store.application.services.create_store import CreateStoreApplicationService
from apps.store.application.services.get_store_by_id import GetStoreApplicationService
from apps.store.domain.store import Store
from apps.store.domain.value_objects.store_id import StoreId
from apps.store.infrastructure.db_entity.store_in_db import StoreInDb
from apps.store.infrastructure.entries.create_store_entry import CreateStoreEntry
from apps.store.infrastructure.mappers.store_mapper import StoreMapper
from apps.store.infrastructure.repositories.db_store_repository import DbStoreRepository
from apps.store.infrastructure.responses.get_all_stores_response import GetAllStoresResponse, StoreResponse
from apps.store.infrastructure.responses.save_store_response import SaveStoreResponse
from apps.user.infrastructure.db_entity.user_in_db import UserInDB
from core.application.decorators.exception_decorator import ExceptionDecorator
from core.infrastructure.events.event_handler_native import NativeEventHandler
from db.db_dependencies import get_database
from loguru import logger
from apps.store.application.services.get_all_stores import GetAllStoresApplicationService

store_router = APIRouter(
    prefix="/store",
    tags=["store"],
    responses={404: {"description": "Not found"}},
)

@store_router.get("/get/{id}", response_model=GetStoreByIdResponseDto, name="store:getById")
async def getStoreById(
    id: UUID,
    db: Database = Depends(get_database),
    current_user: UserInDB = Depends(get_current_active_user),
):

    service = ExceptionDecorator(GetStoreApplicationService(store_repository= DbStoreRepository(db,StoreMapper()), ingredient_repository= DbIngredientsRepository(db,IngredientMapper())))
    response = (await service.execute(StoreId(id))).unwrap()    
    
    return response

@store_router.get("/getall", response_model=GetAllStoresResponse, name="store:getById")
async def getStoreById(
    db: Database = Depends(get_database),
    current_user: UserInDB = Depends(get_current_active_user),
):

    service = ExceptionDecorator(GetAllStoresApplicationService(store_repository= DbStoreRepository(db,StoreMapper())))
    response = (await service.execute(None)).unwrap()
    stores: list[StoreResponse] = []
    for res in response:
        stores.append(StoreResponse(id=res.id.value, name=res.name.value))
    return GetAllStoresResponse(stores=stores)



# @store_router.get("/getall", response_model=GetAllStoresResponse, name="store:getAll")
# async def getStoreById(
#     db: Database = Depends(get_database),
#     current_user: UserInDB = Depends(get_current_active_user),
# ):

#     service = ExceptionDecorator(GetAllStoresApplicationService(store_repository= DbStoresRepository(db,StoreMapper())))
#     response = (await service.execute(None)).unwrap()
#     store: list[GetStoreResponse] = []
#     for res in response:
#         store.append(GetStoreResponse(id=res.id.value, name=res.name.value, quantity=res.quantity.value))
#     return GetAllStoresResponse(store=store)


@store_router.post("/create", response_model=SaveStoreResponse, name="store:create")
async def createStore(
    store: CreateStoreEntry,
    db: Database = Depends(get_database),
    current_user: UserInDB = Depends(get_current_active_user),
):
    event_handler = NativeEventHandler()
    store = CreateStoreDto(**store.dict())
    service = ExceptionDecorator(CreateStoreApplicationService(DbStoreRepository(db,StoreMapper()), event_handler))
    
    return SaveStoreResponse(response=((await service.execute(store)).unwrap()))
