from core.domain.events.domain_event import DomainEvent
from ..value_objects.user_id import UserId
from ..value_objects.user_name import UserName

class UserCreatedEvent(DomainEvent):
    def __init__(self, user_id: UserId, user_name: UserName) -> None:
        super().__init__()
        self.user_id = user_id
        self.user_name = user_name