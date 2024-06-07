from uuid import UUID
from core.domain.value_objects.value_object import ValueObject

class UserId(ValueObject[UUID]):
    def __init__(self, value: UUID) -> None:
        super().__init__(value)

    def equals(self, other: 'UserId') -> bool:
        return self.value == other.value
