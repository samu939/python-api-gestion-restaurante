
from typing import Awaitable
from apps.order.application.dto.get_sells_in_range_dto import GetSellsInRangeDto
from apps.order.domain.order import Order
from apps.order.domain.repositories.order_repository import OrderRepository
from core.application.results.result_wrapper import Result
from core.application.services.application_service import ApplicationService
from apps.user.domain.value_objects.user_id import UserId


class GetSellsInRangeApplicationService(ApplicationService[GetSellsInRangeDto, float]):
    def __init__(self, orders_repository: OrderRepository) -> None:
        self.order_repository = orders_repository

    async def execute(self, input: GetSellsInRangeDto) -> Awaitable[Result[float]]:
        order = await self.order_repository.get_orders_in_range(input.begin, input.end)
        total = 0
        for o in order:
            total += o.price.value
        return Result[float].success(value=total)