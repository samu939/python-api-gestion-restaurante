from apps.plates.domain.exceptions.ingredient_for_plate_quantity_not_valid import IngredientForPlateQuantityNotValid
from core.domain.value_objects.value_object import ValueObject


class IngredientForPlateQuantity (ValueObject[float]):
    
    def __init__ (self, value: float):
        super().__init__(value)
        self.ensureValidState()
    
    def equals(self, other: ValueObject[float]) -> bool:
        return self.value == other.value    
    
    def ensureValidState (self):
        if (self.value == None or self.value < 0):
            raise IngredientForPlateQuantityNotValid()
        