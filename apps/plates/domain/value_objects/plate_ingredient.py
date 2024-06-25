from core.domain.value_objects.value_object import ValueObject
from apps.ingredients.domain.value_objects.ingredient_id import IngredientId
from apps.plates.domain.value_objects.ingredient_for_plate_quantity import IngredientForPlateQuantity
from apps.plates.domain.exceptions.plate_ingredient_not_valid import PlateIngredientNotValid
from apps.plates.domain.exceptions.ingredient_for_plate_quantity_not_valid import IngredientForPlateQuantityNotValid
from apps.ingredients.domain.exceptions.ingredient_id_not_valid_exception import IngredientIdNotValid

class PlateIngredient(ValueObject[dict]):
    
    def __init__(self, value: dict):
        self.ensure_valid_state(value)
        super().__init__(value)
    
    def ensure_valid_state(self, value: dict):
        if not isinstance(value, dict):
            raise PlateIngredientNotValid
        if 'ingredient_id' not in value or 'quantity' not in value:
            raise IngredientIdNotValid
        if not isinstance(value['ingredient_id'], IngredientId):
            raise IngredientIdNotValid
        if not isinstance(value['quantity'], IngredientForPlateQuantity):
            raise IngredientForPlateQuantityNotValid

    def __str__(self):
        return f"PlateIngredient(ingredient_id={self.value['ingredient_id']}, quantity={self.value['quantity']})"
