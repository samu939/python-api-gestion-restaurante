


from typing import Awaitable

from databases import Database
from loguru import logger 
from apps.user.domain.repositories.user_repository import UserRepository
from apps.user.domain.user import User
from apps.user.domain.value_objects.user_id import UserId
from apps.user.infrastructure.db_entity.user_in_db import UserInDB
from apps.user.infrastructure.mappers.user_mapper import UserMapper



class dbUserRepository (UserRepository):
    def __init__(self, db: Database, user_mapper: UserMapper) -> None:
        self.db=db
        self.userMapper = user_mapper
        super().__init__()
        
    async def get_user_by_id(self, id: UserId) -> Awaitable[User | None]:
        from apps.user.infrastructure.queries.user_queries import GET_USER_BY_ID
        values = {"id": id.value}
        logger.info(values)
        record = await self.db.fetch_one(query=GET_USER_BY_ID, values=values)

        if not record:
            return None
        
        return self.userMapper.from_persistence_to_domain(record)
    
    async def get_user_by_username(self, username: str) -> Awaitable[UserInDB | None]:
        from apps.user.infrastructure.queries.user_queries import GET_USER_BY_USERNAME

        values = {"username": username}

        record = await self.db.fetch_one(query=GET_USER_BY_USERNAME, values=values)

        if not record:
            return None

        return UserInDB( id = record.id, name = record.name, username=record.username, password= record.password, role= record.role)
    
    async def add_user(self, user: UserInDB) -> Awaitable[UserInDB | None]:
        from apps.user.infrastructure.queries.user_queries import ADD_USER

        values = {"id": str(user.id), "username": user.username, "password": user.password, "name": user.name, "role": user.role}

        await self.db.execute(query=ADD_USER, values=values)

        return UserInDB( id = user.id, name = user.name, username=user.username, password= user.password, role= user.role)