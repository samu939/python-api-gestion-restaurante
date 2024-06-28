from apps.plates.domain.exceptions.plate_price_not_valid import PlatePriceNotValid
from apps.plates.domain.exceptions.plate_quantity_not_valid_exception import PlateQuantityNotValid
from core.domain.value_objects.value_object import ValueObject


class PlateQuantity (ValueObject[int]):
    
    def __init__ (self, value: int):
        super().__init__(value)
        self.ensureValidState()
    
    def equals(self, other: ValueObject[int]) -> bool:
        return self.value.strip() == other.value.strip()    
    
    def ensureValidState (self):
        if (self.value == None or self.value <= 0):
            raise PlateQuantityNotValid()