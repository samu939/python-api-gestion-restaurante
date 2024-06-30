from uuid import UUID
from databases import Database
from fastapi import APIRouter, Depends

from apps.auth.infraestructure.dependecies.auth_dependecies import get_current_active_user

from apps.ingredients.infrastructure.mappers.ingredient_mapper import IngredientMapper
from apps.ingredients.infrastructure.repositories.db_ingredients_repository import DbIngredientsRepository
from apps.notifications.application.dto.get_all_user_notifications_dto import GetAllUserNotificationsDto
from apps.notifications.application.dto.get_all_user_notifications_reponse_dto import GetAllUserNotificationsResponse
from apps.notifications.application.dto.save_notification_dto import SaveNotificationDto
from apps.notifications.application.services.get_all_user_notifications_application_service import GetAllUserNotificationsApplicationService
from apps.plates.infrastructure.dtos.cook_plate_dto import CookPlateDto
from apps.plates.infrastructure.mappers.plates_mapper import PlateMapper
from apps.user.infrastructure.db_entity.user_in_db import UserInDB
from core.application.decorators.exception_decorator import ExceptionDecorator
from core.infrastructure.events.event_handler_native import NativeEventHandler
from db.db_dependencies import get_database
from apps.plates.infrastructure.repositories.db_plates_repository import DbPlatesRepository
from apps.plates.application.services.cook_plate_application_service import (
    CookPlateApplicationService)
from apps.notifications.application.services.save_notification_application_service import (
    SaveNotificationApplicationService)
from apps.notifications.infrastructure.repositories.db_notification_repository import (
    DbNotificationRepository)


notifications_router = APIRouter(
    prefix="/notifications",
    tags=["notification"],
    responses={404: {"description": "Not found"}},
)


@notifications_router.get("/getall/{user_id}", response_model=GetAllUserNotificationsResponse, name="notification:getAll")
async def getNotifications(
    user_id: UUID,
    db: Database = Depends(get_database),
    current_user: UserInDB = Depends(get_current_active_user)
):
    
    service = ExceptionDecorator(GetAllUserNotificationsApplicationService(notification_repository= DbNotificationRepository(db)))
    
    response = (await service.execute(GetAllUserNotificationsDto(user_id= user_id))).unwrap()
    
    return response
