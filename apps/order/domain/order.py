
from loguru import logger
from apps.order.domain.events.order_created import OrderCreatedEvent
from apps.order.domain.exceptions.invalid_order import OrderNotValid
from apps.order.domain.value_objects.order_date import OrderDate
from apps.order.domain.value_objects.order_id import OrderId
from apps.order.domain.value_objects.order_plate import OrderPlate
from apps.order.domain.value_objects.order_price import OrderPrice
from apps.user.domain.value_objects.user_id import UserId
from core.domain.aggregates.aggregate import Aggregate


class Order (Aggregate[OrderId]):
    def __init__(self, id: OrderId, price: OrderPrice, plates: list[OrderPlate], user_id: UserId, date: OrderDate) -> None:
        super().__init__(id)
        self.user_id = user_id
        self.price = price
        self.plates = plates
        self.date = date
        self.on(OrderCreatedEvent(id, price, plates, user_id, date))

    
    def validate_state(self) -> None:
        if not self.id or not self.price or not self.user_id or not self.date or not self.plates:
            raise OrderNotValid
        self.id.ensureValidState()
        self.price.ensureValidState()
        self.user_id.ensureValidState()
        self.date.ensureValidState()
        for plate in self.plates:
            plate.ensureValidState()