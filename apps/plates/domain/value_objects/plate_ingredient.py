from uuid import UUID
from core.domain.value_objects.value_object import ValueObject
from apps.ingredients.domain.value_objects.ingredient_id import IngredientId
from apps.plates.domain.value_objects.ingredient_for_plate_quantity import IngredientForPlateQuantity
from apps.plates.domain.exceptions.plate_ingredient_not_valid import PlateIngredientNotValid
from apps.plates.domain.exceptions.ingredient_for_plate_quantity_not_valid import IngredientForPlateQuantityNotValid
from apps.ingredients.domain.exceptions.ingredient_id_not_valid_exception import IngredientIdNotValid

class PlateIngredient(ValueObject[dict]):
    
    def __init__(self, value: dict):
        super().__init__(value)
        self.ensureValidState()
    
    def equals(self, other: ValueObject[dict]) -> bool:
        return self.value == other.value    
    
    def ensureValidState(self):
        if not isinstance(self.value, dict):
            raise PlateIngredientNotValid
        if 'ingredient_id' not in self.value or 'quantity' not in self.value:
            raise IngredientIdNotValid
        if not isinstance(self.value['ingredient_id'], IngredientId):
            raise IngredientIdNotValid
        if not isinstance(self.value['quantity'], IngredientForPlateQuantity):
            raise IngredientForPlateQuantityNotValid

    def __str__(self):
        return f"PlateIngredient(ingredient_id={self.value['ingredient_id']}, quantity={self.value['quantity']})"
