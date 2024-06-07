from core.domain.value_objects.value_object import ValueObject

class UserName(ValueObject[str]):
    def __init__(self, value: str) -> None:
        super().__init__(value)

    def equals(self, other: 'UserName') -> bool:
        names = self.value.split()
        other_names = other.value.split()
        if len(names) != len(other_names):
            return False
        result = True
        for i in range(len(names)):
            result = names[i] == other_names[i]
            if not result:
                break
        return result