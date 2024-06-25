from apps.plates.domain.exceptions.plate_name_not_valid_exception import PlateNameNotValid
from core.domain.value_objects.value_object import ValueObject


class PlateName (ValueObject[str]):
    
    def __init__ (self, value: str):
        super().__init__(value)
        self.ensureValidState()
    
    def equals(self, other: ValueObject[str]) -> bool:
        return self.value.strip() == other.value.strip()    
    
    def ensureValidState (self):
        if (self.value == None):
            raise PlateNameNotValid()