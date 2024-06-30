from apps.order.domain.exceptions.invalid_order_price import OrderPriceNotValid
from apps.plates.domain.exceptions.plate_price_not_valid import PlatePriceNotValid
from core.domain.value_objects.value_object import ValueObject


class OrderPrice (ValueObject[float]):
    
    def __init__ (self, value: float):
        super().__init__(value)
        self.ensureValidState()
    
    def equals(self, other: ValueObject[float]) -> bool:
        return self.value.strip() == other.value.strip()    
    
    def ensureValidState (self):
        if (self.value == None):
            raise OrderPriceNotValid()