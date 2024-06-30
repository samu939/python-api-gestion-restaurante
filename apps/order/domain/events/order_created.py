
from apps.order.domain.value_objects.order_date import OrderDate
from apps.order.domain.value_objects.order_id import OrderId
from apps.order.domain.value_objects.order_plate import OrderPlate
from apps.order.domain.value_objects.order_price import OrderPrice
from apps.user.domain.value_objects.user_id import UserId
from core.domain.events.domain_event import DomainEvent

class OrderCreatedEvent(DomainEvent):
    def __init__(self, id: OrderId, order_price: OrderPrice ,order_plates: list[OrderPlate], user_id: UserId, order_date: OrderDate) -> None:
        super().__init__()
        self.id = id
        self.order_price = order_price
        self.order_plates = order_plates
        self.user_id = user_id
        self.order_date = order_date
        