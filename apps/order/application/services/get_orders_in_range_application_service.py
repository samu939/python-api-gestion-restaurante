
from typing import Awaitable
from apps.order.application.dto.get_orders_by_range_response_dto import GetOrderPlateByIdResponse, GetOrdersByRangeResponse
from apps.order.application.dto.get_sells_in_range_dto import GetSellsInRangeDto
from apps.order.domain.order import Order
from apps.order.domain.repositories.order_repository import OrderRepository
from apps.plates.domain.repositories.plates_repository import PlateRepository
from apps.user.domain.repositories.user_repository import UserRepository
from core.application.results.result_wrapper import Result
from core.application.services.application_service import ApplicationService
from apps.user.domain.value_objects.user_id import UserId


class GetOrdersInRangeApplicationService(ApplicationService[GetSellsInRangeDto, list[GetOrdersByRangeResponse]]):
    def __init__(self, orders_repository: OrderRepository, plates_repository: PlateRepository, user_repository: UserRepository) -> None:
        self.order_repository = orders_repository
        self.plates_repository = plates_repository
        self.user_repository = user_repository

    async def execute(self, input: GetSellsInRangeDto) -> Awaitable[Result[list[GetOrdersByRangeResponse]]]:
        orders = await self.order_repository.get_orders_in_range(input.begin, input.end)
        result_orders = []
        for order in orders:
            plates = []
            for plate in order.plates:
                plt = await self.plates_repository.get_plate_by_id(plate.value['plate_id'])
                
                plates.append(GetOrderPlateByIdResponse(id=plate.value['plate_id'].value, 
                                                    name=plt.name.value,
                                                    quantity=plate.value['quantity'].value))
            user = await self.user_repository.get_user_by_id(order.user_id)
            result_orders.append(GetOrdersByRangeResponse(id=order.id.value, date=str(order.date.value), user= user.name.value, price=order.price.value, plates=plates))
        return Result[list[GetOrdersByRangeResponse]].success(value=result_orders)