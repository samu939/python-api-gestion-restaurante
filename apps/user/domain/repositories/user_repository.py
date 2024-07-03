from abc import abstractmethod
from typing import Awaitable, Optional

from apps.user.infrastructure.db_entity.user_in_db import UserInDB
from ..value_objects.user_id import UserId
from ..user import User

class UserRepository:
    @abstractmethod
    def get_user_by_id(self, id: UserId) -> Awaitable[Optional[User]]:
        pass

    @abstractmethod
    def add_user(self, user: UserInDB) -> Awaitable[Optional[User]]:
        pass
    