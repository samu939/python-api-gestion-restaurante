
import bcrypt
import jwt

from apps.auth.application.exceptions.auth_exceptions import AuthExceptions
from apps.auth.infraestructure.entities.token import (
    JWTPayload
)
from pydantic import ValidationError
from config import (
    JWT_ALGORITHM,
    JWT_AUDIENCE,
)
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
class AuthService:
    def get_username_from_token(self, token: str, secret_key: str) -> str | None:
            try:
                decoded_token = jwt.decode(
                    token,
                    str(secret_key),
                    audience=JWT_AUDIENCE,
                    algorithms=[JWT_ALGORITHM],
                )
                payload = JWTPayload(**decoded_token)

            except (jwt.PyJWTError, ValidationError):
                raise AuthExceptions.AuthNoValidTokenCredentialsException()

            except jwt.ExpiredSignatureError:
                raise AuthExceptions.AuthTokenExpiredException()

            return payload.username
        

    def _generate_salt(self) -> str:
        return bcrypt.gensalt().decode()

    def _hash_password(self, *, password: str, salt: str) -> str:
        return pwd_context.hash(password + salt)
