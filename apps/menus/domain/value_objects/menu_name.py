from apps.menus.domain.exceptions.menu_name_not_valid_exception import MenuNameNotValid
from core.domain.value_objects.value_object import ValueObject


class MenuName (ValueObject[str]):
    
    def __init__ (self, value: str):
        super().__init__(value)
        self.ensureValidState()
    
    def equals(self, other: ValueObject[str]) -> bool:
        return self.value.strip() == other.value.strip()    
    
    def ensureValidState (self):
        if (self.value == None):
            raise MenuNameNotValid()