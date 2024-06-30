from uuid import UUID
from apps.order.domain.exceptions.invalid_order_id_exception import OrderIdNotValid
from core.domain.value_objects.value_object import ValueObject


class OrderId (ValueObject[UUID]):
    
    def __init__ (self, value: UUID):
        super().__init__(value)
        self.ensureValidState()
    
    def equals(self, other: ValueObject[UUID]) -> bool:
        return self.value == other.value    
    
    def ensureValidState (self):
        if (self.value == None):
            raise OrderIdNotValid()