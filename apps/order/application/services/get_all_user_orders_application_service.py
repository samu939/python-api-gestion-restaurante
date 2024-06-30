
from typing import Awaitable
from apps.order.application.dto.get_all_user_orders_dto import GetAllUserOrdersDto
from apps.order.domain.order import Order
from apps.order.domain.repositories.order_repository import OrderRepository
from core.application.results.result_wrapper import Result
from core.application.services.application_service import ApplicationService
from apps.user.domain.value_objects.user_id import UserId


class GetAllUserOrdersApplicationService(ApplicationService[GetAllUserOrdersDto, list[Order]]):
    def __init__(self, orders_repository: OrderRepository) -> None:
        self.order_repository = orders_repository

    async def execute(self, input: GetAllUserOrdersDto) -> Awaitable[Result[list[Order]]]:
        order = await self.order_repository.get_all_orders_by_user(UserId(input.user_id))
        return Result[list[Order]].success(value=order)