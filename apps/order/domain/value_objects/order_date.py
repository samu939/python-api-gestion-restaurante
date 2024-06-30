
from datetime import datetime
from uuid import UUID
from apps.order.domain.exceptions.invalid_order_date import OrderDateNotValid
from core.domain.value_objects.value_object import ValueObject


class OrderDate (ValueObject[datetime]):
    
    def __init__ (self, value: datetime):
        super().__init__(value)
        self.ensureValidState()
    
    def equals(self, other: ValueObject[datetime]) -> bool:
        return self.value == other.value    
    
    def ensureValidState (self):
        if (self.value == None):
            raise OrderDateNotValid()