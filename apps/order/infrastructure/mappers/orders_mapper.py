

import json
from apps.order.domain.order import Order

from apps.order.domain.value_objects.order_date import OrderDate
from apps.order.domain.value_objects.order_id import OrderId
from apps.order.domain.value_objects.order_plate_quantity import OrderPlateQuantity
from apps.order.domain.value_objects.order_price import OrderPrice
from apps.plates.domain.value_objects.plate_id import PlateId
from core.application.mappers.mapper import Mapper
from apps.order.domain.value_objects.order_plate import OrderPlate
from apps.user.domain.value_objects.user_id import UserId


class OrderMapper(Mapper[Order, dict[str, str]]):
    def __init__(self) -> None:
        super().__init__()
    
    def from_domain_to_persistence(self, domain_entity: Order):
        pass
    
    def from_persistence_to_domain(self, persistence_entity: dict[str, str]) -> Order:

        plates = []

        for plate in json.loads(persistence_entity['plates']):
            plates.append({
                'plate_id': PlateId(plate['plate_id']),
                'quantity': OrderPlateQuantity(plate['quantity'])
            })

        return Order(
            OrderId(persistence_entity['id']),
            OrderPrice(persistence_entity['price']),
            [OrderPlate(plate) for plate in plates],
            UserId(persistence_entity['user_id']),
            OrderDate(persistence_entity['date']),
        )