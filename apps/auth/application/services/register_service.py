
from uuid import uuid4
import bcrypt
from apps.auth.application.dto.login_dto import loginDto
from apps.auth.application.dto.login_response import AuthResponse
from apps.auth.application.exceptions.auth_exceptions import AuthExceptions
from apps.auth.application.token.token_generator import tokenGenerator
from apps.user.domain.repositories.user_repository import UserRepository
from apps.user.infrastructure.db_entity.user_in_db import UserInDB
from apps.user.infrastructure.register_entry import RegisterUserEntry
from core.application.results.result_wrapper import Result
from core.application.services.application_service import ApplicationService
from databases import Database
from loguru import logger

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class registerService (ApplicationService):
    
    def __init__(self, db: Database, user_repository: UserRepository, token_generator: tokenGenerator) -> None:
        self.db = db
        self.user_repository = user_repository
        self.token_generator = token_generator
        super().__init__()
        
    
    def verify_password(self, password: str, hashed_pw: str) -> bool:
        return pwd_context.verify(password, hashed_pw)
    
    async def execute (self, input: RegisterUserEntry)-> Result[AuthResponse]:

        if not input.name:
            logger.error("Try to register without name")
            return Result[AuthResponse].failure(error = AuthExceptions.AuthNoUsernameException())
        if not input.username:
            logger.error("Try to register without username")
            return Result[AuthResponse].failure(error = AuthExceptions.AuthNoUsernameException())
        if not input.password:
            logger.error("Try to register without password")
            return Result[AuthResponse].failure(error =AuthExceptions.AuthNoPasswordException())
        if not input.role:
            logger.error("Try to register without a role")
            return Result[AuthResponse].failure(error =AuthExceptions.AuthNoRoleException())

        user = await self.user_repository.get_user_by_username(username=input.username)

        if user:
            logger.error(f"Trying to register with existing username: {input.username}")
            return Result[AuthResponse].failure(error =AuthExceptions.AuthDuplicatedUsernameException())
        
        password_in_bytes = input.password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password_in_bytes, salt)
        
        hashed_password_str = hashed_password.decode('utf-8')

        new_user = UserInDB(id=str(uuid4()), username=input.username, password=hashed_password_str, name=input.name, role=input.role)
        await self.user_repository.add_user(new_user)

        user_autenticated = AuthResponse(
            access_token=self.token_generator.generate(user=new_user),
            token_type="bearer",
            id=new_user.id,
            name=new_user.name,
            username=new_user.username,
            role=new_user.role,
        )

        return Result[AuthResponse].success(user_autenticated)
    
   