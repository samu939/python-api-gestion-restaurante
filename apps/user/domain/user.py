from core.domain.aggregates.aggregate import Aggregate
from .value_objects.user_id import UserId
from .value_objects.user_name import UserName
from .events.user_created import UserCreatedEvent
from .exceptions.invalid_user import InvalidUserException

class User(Aggregate[UserId]):
    def __init__(self, id: UserId, name: UserName) -> None:
        super().__init__(id)
        self._name = name
        self.on(UserCreatedEvent(id, name))
    
    @property
    def name(self) -> UserName:
        return self._name
    
    def validate_state(self) -> None:
        if not self._name or not self._id:
            raise InvalidUserException()
    