
from typing import Awaitable
from apps.notifications.application.notification_repository import NotificationRepository
from apps.order.application.dto.get_all_user_orders_dto import GetAllUserOrdersDto
from apps.order.domain.order import Order
from apps.order.domain.repositories.order_repository import OrderRepository
from core.application.results.result_wrapper import Result
from core.application.services.application_service import ApplicationService
from apps.user.domain.value_objects.user_id import UserId
from apps.notifications.application.dto.get_all_user_notifications_dto import (
    GetAllUserNotificationsDto)
from apps.notifications.application.dto.get_all_user_notifications_reponse_dto import (
    GetAllUserNotificationsResponse,
    Notification)


class GetAllUserNotificationsApplicationService(ApplicationService[GetAllUserNotificationsDto, GetAllUserNotificationsResponse]):
    def __init__(self, notification_repository: NotificationRepository) -> None:
        self.notification_repository = notification_repository

    async def execute(self, input: GetAllUserNotificationsDto) -> Awaitable[Result[list[GetAllUserNotificationsResponse]]]:
        notis = await self.notification_repository.get_all_notifications_by_user(input.user_id)
        noti = []
        for notification in notis:
            noti.append(Notification(id=notification.id, message=notification.message, date=notification.date.__str__(), target_user=notification.target_user))
            
        
        return Result[list[GetAllUserNotificationsResponse]].success(value=GetAllUserNotificationsResponse(notifications=noti))