from uuid import UUID
from databases import Database
from fastapi import APIRouter, Depends
from apps.auth.infraestructure.dependecies.auth_dependecies import get_current_active_user, role_required
from apps.ingredients.application.dto.create_ingredient_dto import CreateIngredientDto
from apps.ingredients.application.dto.ingredient_change_store_dto import IngredientChangeStoreDto
from apps.ingredients.application.dto.modify_ingredient_quantity_dto import ModifyIngredientQuantityDto
from apps.ingredients.application.services.change_ingredient_store import ChangeIngredientStoreApplicationService
from apps.ingredients.application.services.create_ingredient import CreateIngredientApplicationService
from apps.ingredients.application.services.egress_ingredient import EgressIngredientApplicationService
from apps.ingredients.application.services.get_all_ingredients import GetAllIngredientsApplicationService
from apps.ingredients.application.services.get_ingredient import GetIngredientApplicationService
from apps.ingredients.application.services.ingress_ingredient import IngressIngredientApplicationService
from apps.ingredients.domain.value_objects.ingredient_id import IngredientId
from apps.ingredients.infrastructure.entries.create_ingredient_entry import CreateIngredientEntry
from apps.ingredients.infrastructure.entries.modify_quantity_entry import ModifyQuantityEntry
from apps.ingredients.infrastructure.entries.modify_store_entry import ModifyStoreEntry
from apps.ingredients.infrastructure.mappers.ingredient_mapper import IngredientMapper
from apps.ingredients.infrastructure.repositories.db_ingredients_repository import DbIngredientsRepository
from apps.ingredients.infrastructure.responses.ingredients_responses import GetAllIngredientsResponse, GetIngredientResponse, SaveIngredientResponse
from apps.store.infrastructure.mappers.store_mapper import StoreMapper
from apps.store.infrastructure.repositories.db_store_repository import DbStoreRepository
from apps.user.infrastructure.db_entity.user_in_db import UserInDB, roleEnum
from core.application.decorators.exception_decorator import ExceptionDecorator
from core.infrastructure.events.event_handler_native import NativeEventHandler
from db.db_dependencies import get_database
from loguru import logger

ingredient_router = APIRouter(
    prefix="/ingredient",
    tags=["ingredient"],
    responses={404: {"description": "Not found"}},
)

@ingredient_router.get("/get/{id}", response_model=GetIngredientResponse, name="ingredient:getById")
async def getIngredientById(
    id: UUID,
    db: Database = Depends(get_database),
    current_user: UserInDB = Depends(role_required([roleEnum.administrador, roleEnum.chef, roleEnum.camarero])),
):

    service = ExceptionDecorator(GetIngredientApplicationService(ingredient_repository= DbIngredientsRepository(db,IngredientMapper())))
    response = (await service.execute(IngredientId(id))).unwrap()
    return GetIngredientResponse(id=response.id.value, name=response.name.value, quantity=response.quantity.value, storeId=response.storeId.value)

@ingredient_router.get("/getall", response_model=GetAllIngredientsResponse, name="ingredient:getAll")
async def getIngredients(
    db: Database = Depends(get_database),
    current_user: UserInDB = Depends(role_required([roleEnum.administrador, roleEnum.chef, roleEnum.camarero])),
):

    service = ExceptionDecorator(GetAllIngredientsApplicationService(ingredient_repository= DbIngredientsRepository(db,IngredientMapper())))
    response = (await service.execute(None)).unwrap()
    ingredients: list[GetIngredientResponse] = []
    for res in response:
        ingredients.append(GetIngredientResponse(id=res.id.value, name=res.name.value, quantity=res.quantity.value, storeId=res.storeId.value))
    return GetAllIngredientsResponse(ingredients=ingredients)


@ingredient_router.post("/create", response_model=SaveIngredientResponse, name="ingredient:create")
async def createIngredient(
    new_ingredient: CreateIngredientEntry,
    db: Database = Depends(get_database),
    current_user: UserInDB = Depends(role_required([roleEnum.administrador, roleEnum.chef])),
):
    event_handler = NativeEventHandler()
    print(new_ingredient)
    ingredient = CreateIngredientDto(**new_ingredient.dict())
    service = ExceptionDecorator(CreateIngredientApplicationService(DbIngredientsRepository(db,IngredientMapper()), store_repository= DbStoreRepository(db,StoreMapper()), event_handler=event_handler))
    
    return SaveIngredientResponse(response=((await service.execute(ingredient)).unwrap()))

@ingredient_router.post("/ingress/{id}", response_model=GetIngredientResponse, name="ingredient:ingress")
async def ingressIngredient(
    id: UUID,
    quantity: ModifyQuantityEntry,
    db: Database = Depends(get_database),
    current_user: UserInDB = Depends(role_required([roleEnum.administrador, roleEnum.chef])),
):
    logger.info(quantity)
    event_handler = NativeEventHandler()
    service = ExceptionDecorator(IngressIngredientApplicationService(DbIngredientsRepository(db,IngredientMapper()),event_handler)
    )
    service_dto = ModifyIngredientQuantityDto(ingredient_id=id, quantity=quantity.quantity)
    response = (await service.execute(service_dto)).unwrap()
    return GetIngredientResponse(id=response.id.value, name=response.name.value, quantity=response.quantity.value, storeId=response.storeId.value)


@ingredient_router.post("/egress/{id}", response_model=GetIngredientResponse, name="ingredient:egress")
async def ingressIngredient(
    id: UUID,
    quantity: ModifyQuantityEntry,
    db: Database = Depends(get_database),
    current_user: UserInDB = Depends(role_required([roleEnum.administrador, roleEnum.chef])),
):
    event_handler = NativeEventHandler()
    service = ExceptionDecorator(EgressIngredientApplicationService(DbIngredientsRepository(db,IngredientMapper()),event_handler)
    )
    service_dto = ModifyIngredientQuantityDto(ingredient_id=id, quantity=quantity.quantity)
    response = (await service.execute(service_dto)).unwrap()
    return GetIngredientResponse(id=response.id.value, name=response.name.value, quantity=response.quantity.value, storeId=response.storeId.value)

@ingredient_router.post("/changestore/{id}", response_model=GetIngredientResponse, name="ingredient:changeStore")
async def ingressIngredient(
    id: UUID,
    store_id: ModifyStoreEntry,
    db: Database = Depends(get_database),
    current_user: UserInDB = Depends(role_required([roleEnum.administrador, roleEnum.chef])),
):
    event_handler = NativeEventHandler()
    service = ExceptionDecorator(ChangeIngredientStoreApplicationService(DbIngredientsRepository(db,IngredientMapper()),event_handler)
    )
    service_dto = IngredientChangeStoreDto(ingredient_id=id, store_id=store_id.store_id)
    response = (await service.execute(service_dto)).unwrap()
    return GetIngredientResponse(id=response.id.value, name=response.name.value, quantity=response.quantity.value, storeId=response.storeId.value)