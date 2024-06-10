
from apps.auth.application.dto.login_dto import loginDto
from apps.auth.application.dto.login_response import AuthResponse
from apps.auth.application.exceptions.auth_exceptions import AuthExceptions
from apps.auth.application.token.token_generator import tokenGenerator
from apps.user.domain.repositories.user_repository import UserRepository
from core.application.results.result_wrapper import Result
from core.application.services.application_service import ApplicationService
from databases import Database
from loguru import logger

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class loginService (ApplicationService):
    
    def __init__(self, db: Database, user_repository: UserRepository, token_generator: tokenGenerator) -> None:
        self.db = db
        self.user_repository = user_repository
        self.token_generator = token_generator
        super().__init__()
        
    
    def verify_password(self, password: str, hashed_pw: str) -> bool:
        return pwd_context.verify(password, hashed_pw)
    
    async def execute (self, input: loginDto)-> Result[AuthResponse]:

        if not input.username:
            logger.error("Try to login without username")
            return Result[AuthResponse].failure(error = AuthExceptions.AuthNoUsernameException())

        if not input.password:
            logger.error("Try to login without password")
            return Result[AuthResponse].failure(error =AuthExceptions.AuthNoPasswordException())

        user = await self.user_repository.get_user_by_username(username=input.username)

        if not user:
            logger.error(f"Trying to login with invalid credentials, username: {input.username}")
            return Result[AuthResponse].failure(error =AuthExceptions.AuthNoValidCredencialsException())

        if not self.verify_password(password=input.password, hashed_pw=user.password):
            logger.error(f"Trying to login with invalid credentials, username: {input.username}")
            return Result[AuthResponse].failure(error =AuthExceptions.AuthNoValidCredencialsException())

        user_autenticated = AuthResponse(
            access_token=self.token_generator.generate(user=user),
            token_type="bearer",
            id=user.id,
            name=user.name,
            username=user.username,
            role=user.role,
        )

        return Result[AuthResponse].success(user_autenticated)
    
   