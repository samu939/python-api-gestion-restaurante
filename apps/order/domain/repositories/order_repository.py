from abc import abstractmethod
from datetime import date
from typing import Awaitable, Optional

from apps.order.domain.order import Order
from apps.order.domain.value_objects.order_id import OrderId
from apps.user.domain.value_objects.user_id import UserId

class OrderRepository:
    @abstractmethod
    def get_order_by_id(self, id: OrderId) -> Awaitable[Optional[Order]]:
        pass
    @abstractmethod
    def get_all_orders_by_user(self, user_id: UserId) -> Awaitable[list[Order]]:
        pass
    @abstractmethod
    def save_order(self, order: Order) -> Awaitable[None]:
        pass
    @abstractmethod
    def get_orders_in_range(self, start: date, end: date) -> Awaitable[list[Order]]:
        pass
