from apps.ingredients.domain.exceptions.ingredient_quantity_not_valid_exception import IngredientQuantityNotValid
from core.domain.value_objects.value_object import ValueObject


class IngredientQuantity (ValueObject[int]):
    
    def __init__ (self, value: int):
        super().__init__(value)
        self.ensureValidState()
    
    def equals(self, other: ValueObject[int]) -> bool:
        return self.value == other.value    
    
    def ensureValidState (self):
        if (self.value == None or self.value < 0):
            raise IngredientQuantityNotValid()