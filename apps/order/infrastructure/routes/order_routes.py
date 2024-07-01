from uuid import UUID
from databases import Database
from fastapi import APIRouter, Depends

from apps.auth.infraestructure.dependecies.auth_dependecies import get_current_active_user

from apps.ingredients.infrastructure.mappers.ingredient_mapper import IngredientMapper
from apps.ingredients.infrastructure.repositories.db_ingredients_repository import DbIngredientsRepository
from apps.notifications.application.dto.save_notification_dto import SaveNotificationDto
from apps.order.application.dto.create_order_dto import CreateOrderDto
from apps.order.application.dto.get_all_user_orders_dto import GetAllUserOrdersDto
from apps.order.application.dto.get_order_by_id_dto import GetOrderByIdDto
from apps.order.application.dto.get_order_by_id_response_dto import GetOrderByIdResponse
from apps.order.application.services.create_order_application_service import CreateOrderApplicationService
from apps.order.application.services.get_all_user_orders_application_service import GetAllUserOrdersApplicationService
from apps.order.application.services.get_order_by_id_application_service import GetOrderByIdApplicationService
from apps.order.domain.value_objects.order_id import OrderId
from apps.order.infrastructure.entries.create_order_entry import CreateOrderEntry
from apps.order.infrastructure.mappers.orders_mapper import OrderMapper
from apps.order.infrastructure.repositories.db_orders_repository import DbOrdersRepository
from apps.order.infrastructure.responses.order_responses import GetAllOrdersResponse, GetOrderPlateResponse, GetOrderResponse, SaveOrderResponse
from apps.plates.application.dtos.cook_plate_dto import CookPlateDto
from apps.plates.infrastructure.mappers.plates_mapper import PlateMapper
from apps.user.infrastructure.db_entity.user_in_db import UserInDB
from core.application.decorators.exception_decorator import ExceptionDecorator
from core.infrastructure.events.event_handler_native import NativeEventHandler
from db.db_dependencies import get_database
from apps.plates.infrastructure.repositories.db_plates_repository import DbPlatesRepository
from apps.order.domain.events.order_created import OrderCreatedEvent
from apps.plates.application.services.cook_plate_application_service import (
    CookPlateApplicationService)
from apps.notifications.application.services.save_notification_application_service import (
    SaveNotificationApplicationService)
from apps.notifications.infrastructure.repositories.db_notification_repository import (
    DbNotificationRepository)


orders_router = APIRouter(
    prefix="/orders",
    tags=["order"],
    responses={404: {"description": "Not found"}},
)

@orders_router.post("/create", response_model=SaveOrderResponse, name="order:create")
async def createOrder(
    new_order: CreateOrderEntry,
    db: Database = Depends(get_database),
    current_user: UserInDB = Depends(get_current_active_user)
):
    event_handler = NativeEventHandler()
    
    async def proccess_order (event: OrderCreatedEvent):
        service = CookPlateApplicationService(plates_repository= DbPlatesRepository(db, PlateMapper()), 
                                              ingredients_repository= DbIngredientsRepository(db, IngredientMapper()), 
                                              event_handler=event_handler)
        noti_service = SaveNotificationApplicationService(notification_repository= DbNotificationRepository(db))
        errors = []
        for plate in event.order_plates:
            result = await service.execute(CookPlateDto(plate_id=plate.value['plate_id'], quantity=plate.value['quantity']))
            if result.is_error():
                await noti_service.execute(SaveNotificationDto(message=f'plato {plate.value["plate_id"].value} no se pudo cocinar', target_user=current_user.id))
            else: 
                await noti_service.execute(SaveNotificationDto(message=f'plato {plate.value["plate_id"].value} cocinado, cantidad: {plate.value["quantity"].value}', target_user=current_user.id))
        print(errors)
        return errors
    unsuscribe = event_handler.subscribe(
        OrderCreatedEvent.__name__,
        proccess_order
    )
    order = CreateOrderDto(**new_order.dict(), user_id=current_user.id)
    service = ExceptionDecorator(CreateOrderApplicationService(plates_repository= DbPlatesRepository(db, PlateMapper()),orders_repository= DbOrdersRepository(db, OrderMapper()), event_handler=event_handler))
    response = (await service.execute(order)).unwrap()
    unsuscribe()
    return SaveOrderResponse(response=response)

@orders_router.get("/getall/{user_id}", response_model=GetAllOrdersResponse, name="order:getAll")
async def getOrders(
    user_id: UUID,
    db: Database = Depends(get_database),
    current_user: UserInDB = Depends(get_current_active_user)
):
    
    service = ExceptionDecorator(GetAllUserOrdersApplicationService(orders_repository= DbOrdersRepository(db, OrderMapper())))
    
    response = (await service.execute(GetAllUserOrdersDto(user_id= user_id))).unwrap()
    orders: list[GetOrderResponse] = []
    
    for order in response:
        orders.append(GetOrderResponse(id=order.id.value, date=order.date.value.__str__(), user_id=order.user_id.value,
                                       price=order.price.value, 
                                       plates=[
                                           GetOrderPlateResponse(id=plate.value['plate_id'].value, 
                                            quantity=plate.value['quantity'].value) for plate in order.plates]))
    
    return GetAllOrdersResponse(orders=orders)


@orders_router.get("/get/{id}", response_model=GetOrderByIdResponse, name="order:getAll")
async def getOrders(
    id: UUID,
    db: Database = Depends(get_database),
    current_user: UserInDB = Depends(get_current_active_user)
):
    
    service = ExceptionDecorator(GetOrderByIdApplicationService(plates_repository= DbPlatesRepository(db, PlateMapper()),orders_repository= DbOrdersRepository(db, OrderMapper())))    
    
    return (await service.execute(GetOrderByIdDto(id= id))).unwrap()