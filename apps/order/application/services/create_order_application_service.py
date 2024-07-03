from datetime import date, datetime
from typing import Awaitable
from uuid import uuid4
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
from apps.plates.application.errors.plate_not_found import PlateNotFoundApplicatonError


class CreateOrderApplicationService(ApplicationService[CreateOrderDto, str]):
    def __init__(self, orders_repository: OrderRepository, plates_repository: PlateRepository, event_handler: EventHandler) -> None:
        self.orders_repository = orders_repository
        self.event_handler = event_handler
        self.plates_repository = plates_repository
    async def execute(self, input: CreateOrderDto) -> Awaitable[Result[str]]:

        domain_order_plates = []
        price = 0
        for plate in input.plates:
            domain_order_plates.append(OrderPlate({
                'plate_id': PlateId(plate.id),
                'quantity': OrderPlateQuantity(plate.quantity)
            }))
            plt = await self.plates_repository.get_plate_by_id(PlateId(plate.id))
            if plt is None:
                return Result[str].failure(error= PlateNotFoundApplicatonError(PlateId(plate.id)))
            price += plt.price.value * plate.quantity
        
        

        domain_order = Order(OrderId(str(uuid4())),
                             OrderPrice(price), domain_order_plates,
                             UserId(input.user_id), OrderDate(datetime.now()))
        await self.event_handler.publish_events(domain_order.pull_events())
        await self.orders_repository.save_order(domain_order)
        return Result[str].success(value="Orden guardada") # type: ignore
