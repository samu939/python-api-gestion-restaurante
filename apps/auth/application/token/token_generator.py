


from abc import ABC, abstractmethod

from apps.user.infrastructure.db_entity.user_in_db import UserInDB


class tokenGenerator(ABC):
    
    @abstractmethod
    def generate (self,
        *,
        user: UserInDB) -> str:
        pass