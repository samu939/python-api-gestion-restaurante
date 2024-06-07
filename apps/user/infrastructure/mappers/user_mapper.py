from apps.user.domain.user import User
from apps.user.domain.value_objects.user_id import UserId
from apps.user.domain.value_objects.user_name import UserName
from core.application.mappers.mapper import Mapper

class UserMapper(Mapper[User, dict[str, str]]):
    def __init__(self) -> None:
        super().__init__()

    def from_domain_to_persistence(self, domain_entity: User) -> dict[str, str]:
        return {
            'id': domain_entity.id.value,
            'name': domain_entity.name.value
        }

    def from_persistence_to_domain(self, persistence_entity: dict[str, str]) -> User:
        return User(
            UserId(persistence_entity['id']),
            UserName(persistence_entity['name'])
        )