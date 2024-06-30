
from typing import Awaitable
from databases import Database

from apps.order.domain.order import Order
from apps.order.domain.repositories.order_repository import OrderRepository
from apps.order.domain.value_objects.order_id import OrderId
from apps.order.infrastructure.mappers.orders_mapper import OrderMapper
from apps.plates.domain.plate import Plate
from apps.plates.domain.value_objects.plate_id import PlateId
from apps.user.domain.value_objects.user_id import UserId



class DbOrdersRepository(OrderRepository):
    def __init__(self, db: Database, order_mapper: OrderMapper) -> None:
        self.db = db
        self.order_mapper = order_mapper
        super().__init__()

    async def get_all_orders_by_user(self, user_id: UserId) -> Awaitable[list[Order]]:
        from apps.order.infrastructure.queries.order_queries import GET_ALL_ORDERS_BY_USERS
        records = await self.db.fetch_all(query=GET_ALL_ORDERS_BY_USERS, values={'user_id': str(user_id.value)})
        return [self.order_mapper.from_persistence_to_domain(record) for record in records]
    
    async def get_order_by_id(self, id: OrderId) -> Awaitable[Order | None]:
        from apps.order.infrastructure.queries.order_queries import GET_ORDER_BY_ID
        
        record = await self.db.fetch_one(query=GET_ORDER_BY_ID, values={'id': str(id.value)})

        return self.order_mapper.from_persistence_to_domain(record)

    async def save_order(self, order: Order) -> Awaitable[None]:
        from apps.order.infrastructure.queries.order_queries import INSERT_NEW_ORDER, INSERT_NEW_ORDER_DETAIL

        res = await self.db.execute(query=INSERT_NEW_ORDER, values={
            'id': str(order.id.value),
            'date': order.date.value,
            'price': order.price.value,
            'user_id': str(order.user_id.value)
        })

        print(res)

        for plate in order.plates:
            await self.db.execute(query=INSERT_NEW_ORDER_DETAIL, values={
                'order_id': order.id.value,
                'plate_id': str(plate.value['plate_id'].value),
                'quantity': plate.value['quantity'].value
            })
