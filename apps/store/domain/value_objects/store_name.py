from apps.ingredients.domain.exceptions.ingredient_name_not_valid_exception import IngredientNameNotValid
from apps.store.domain.exceptions.inventory_name_not_valid_exception import InventoryNameNotValid
from core.domain.value_objects.value_object import ValueObject


class StoreName (ValueObject[str]):
    
    def __init__ (self, value: str):
        super().__init__(value)
        self.ensureValidState()
    
    def equals(self, other: ValueObject[str]) -> bool:
        return self.value.strip() == other.value.strip()    
    
    def ensureValidState (self):
        if (len(self.value) < 2):
            raise InventoryNameNotValid()