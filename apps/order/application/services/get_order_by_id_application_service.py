from datetime import date, datetime
from typing import Awaitable
from uuid import uuid4
from apps.order.application.dto.create_order_dto import CreateOrderDto
from apps.order.application.dto.get_order_by_id_dto import GetOrderByIdDto
from apps.order.application.dto.get_order_by_id_response_dto import GetOrderByIdResponse, GetOrderPlateByIdResponse
from apps.order.application.errors.order_not_found import OrderNotFoundApplicatonError
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


class GetOrderByIdApplicationService(ApplicationService[GetOrderByIdDto, GetOrderByIdResponse]):
    def __init__(self, orders_repository: OrderRepository, plates_repository: PlateRepository) -> None:
        self.orders_repository = orders_repository
        self.plates_repository = plates_repository
    async def execute(self, input: GetOrderByIdDto) -> Awaitable[Result[GetOrderByIdResponse]]:

        order = await self.orders_repository.get_order_by_id(OrderId(input.id))
        if not order:
            return Result[GetOrderByIdResponse].failure(error= OrderNotFoundApplicatonError(input.id))
        plates = []
        for plate in order.plates:
            plt = await self.plates_repository.get_plate_by_id(plate.value['plate_id'])
            plates.append(GetOrderPlateByIdResponse(id=plate.value['plate_id'].value, 
                                                    name=plt.name.value,
                                                    quantity=plate.value['quantity'].value))
        
        response = GetOrderByIdResponse(id=order.id.value, date=order.date.value.__str__(), user_id=order.user_id.value,
                                        price=order.price.value, 
                                        plates=plates)
        
        return Result[GetOrderByIdResponse].success(value=response) # type: ignore
