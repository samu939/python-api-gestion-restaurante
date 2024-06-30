from apps.order.domain.exceptions.order_plate_quantity_not_valid import OrderPlateQuantityNotValid
from core.domain.value_objects.value_object import ValueObject



class OrderPlateQuantity (ValueObject[float]):
    
    def __init__ (self, value: float):
        super().__init__(value)
        self.ensureValidState()
    
    def equals(self, other: ValueObject[float]) -> bool:
        return self.value == other.value    
    
    def ensureValidState (self):
        if (self.value == None or self.value < 0):
            raise OrderPlateQuantityNotValid()
        