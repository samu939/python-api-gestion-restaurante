from uuid import UUID
from apps.plates.domain.exceptions.plate_id_not_valid_exception import PlateIdNotValid
from core.domain.value_objects.value_object import ValueObject


class PlateId (ValueObject[UUID]):
    
    def __init__ (self, value: UUID):
        super().__init__(value)
        self.ensureValidState()
    
    def equals(self, other: ValueObject[UUID]) -> bool:
        return self.value == other.value    
    
    def ensureValidState (self):
        if (self.value == None):
            raise PlateIdNotValid()