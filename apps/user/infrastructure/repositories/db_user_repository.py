


from typing import Awaitable

from databases import Database
from apps.user.domain.repositories.user_repository import UserRepository
from apps.user.domain.user import User
from apps.user.domain.value_objects.user_id import UserId
from apps.user.infrastructure.db_entity.user_in_db import UserInDB



class dbUserRepository (UserRepository):
    def __init__(self, db: Database) -> None:
        self.db=db
        super().__init__()
        
    def get_user_by_id(self, id: UserId) -> Awaitable[User | None]:
        return super().get_user_by_id(id)
    
    async def get_user_by_username(self, username: str) -> Awaitable[UserInDB | None]:
        from apps.user.infrastructure.queries.user_queries import GET_USER_BY_USERNAME

        values = {"username": username}
        record = await self.db.fetch_one(query=GET_USER_BY_USERNAME, values=values)

        if not record:
            return None

        return UserInDB( id = record.id, name = record.name, username=record.username, password= record.password, role= record.role)