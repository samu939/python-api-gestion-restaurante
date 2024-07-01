from uuid import UUID
from apps.menus.domain.exceptions.menu_id_not_valid_exception import MenuIdNotValid
from core.domain.value_objects.value_object import ValueObject


class MenuId (ValueObject[UUID]):
    
    def __init__ (self, value: UUID):
        super().__init__(value)
        self.ensureValidState()
    
    def equals(self, other: ValueObject[UUID]) -> bool:
        return self.value == other.value    
    
    def ensureValidState (self):
        if (self.value == None):
            raise MenuIdNotValid()