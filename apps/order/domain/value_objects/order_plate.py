from uuid import UUID
from apps.order.domain.exceptions.order_plate_not_valid import OrderPlateNotValid
from apps.order.domain.exceptions.order_plate_quantity_not_valid import OrderPlateQuantityNotValid
from .order_plate_quantity import OrderPlateQuantity
from apps.plates.domain.value_objects.plate_id import PlateId
from core.domain.value_objects.value_object import ValueObject

class OrderPlate(ValueObject[dict]):
    
    def __init__(self, value: dict):
        super().__init__(value)
        self.ensureValidState()
    
    def equals(self, other: ValueObject[dict]) -> bool:
        return self.value == other.value    
    
    def ensureValidState(self):
        if not isinstance(self.value, dict):
            raise OrderPlateNotValid
        if 'plate_id' not in self.value or 'quantity' not in self.value:
            raise OrderPlateNotValid
        if not isinstance(self.value['plate_id'], PlateId):
            raise OrderPlateNotValid
        if not isinstance(self.value['quantity'], OrderPlateQuantity):
            raise OrderPlateQuantityNotValid

    def __str__(self):
        return f"OrderPlates(plate_id={self.value['plate_id']}, quantity={self.value['quantity']})"
