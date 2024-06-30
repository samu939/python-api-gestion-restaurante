from datetime import date, datetime
from typing import Awaitable
from uuid import uuid4
from apps.notifications.application.dto.save_notification_dto import SaveNotificationDto
from apps.order.application.dto.create_order_dto import CreateOrderDto
from apps.order.domain.order import Order
from apps.order.domain.repositories.order_repository import OrderRepository
from apps.order.domain.value_objects.order_date import OrderDate
from apps.order.domain.value_objects.order_id import OrderId
from apps.order.domain.value_objects.order_plate import OrderPlate
from apps.order.domain.value_objects.order_plate_quantity import OrderPlateQuantity
from apps.order.domain.value_objects.order_price import OrderPrice
from apps.plates.domain.repositories.plates_repository import PlateRepository
from apps.plates.domain.value_objects.plate_id import PlateId
from apps.user.domain.value_objects.user_id import UserId
from core.application.events.event_handler import EventHandler
from core.application.results.result_wrapper import Result
from core.application.services.application_service import ApplicationService
from apps.notifications.application.notification_repository import NotificationRepository


class SaveNotificationApplicationService(ApplicationService[SaveNotificationDto, str]):
    def __init__(self, notification_repository: NotificationRepository) -> None:
        self.notification_repository = notification_repository

    async def execute(self, input: SaveNotificationDto) -> Awaitable[Result[str]]:

        await self.notification_repository.save_notification(str(uuid4()),input.message, input.target_user)
        return Result[str].success(value="Orden guardada") # type: ignore
