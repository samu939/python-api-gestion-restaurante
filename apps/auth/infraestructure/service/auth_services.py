
import bcrypt
import jwt
from datetime import datetime, timedelta, timezone
from apps.auth.application.exceptions.auth_exceptions import AuthExceptions
from apps.auth.infraestructure.entities.token import (
    JWTCreds,
    JWTMeta,
    JWTPayload
)
from pydantic import ValidationError
from apps.user.infrastructure.db_entity.user_in_db import UserInDB
from config import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    JWT_ALGORITHM,
    JWT_AUDIENCE,
    SECRET_KEY,
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
    
    
    def create_access_token_for_user(
        self,
        *,
        user: UserInDB,
        secret_key: str = str(SECRET_KEY),
        audience: str = JWT_AUDIENCE,
        expires_in: int = ACCESS_TOKEN_EXPIRE_MINUTES,
    ) -> str:
        if not user or not isinstance(user, UserInDB):
            return None

        creation_time = datetime.now().replace(tzinfo=None)
        expire_time = creation_time + timedelta(minutes=expires_in)

        jwt_meta = JWTMeta(
            aud=audience,
            iat=datetime.timestamp(creation_time),
            exp=datetime.timestamp(expire_time),
        )

        jwt_creds = JWTCreds(username=user.username)
        token_payload = JWTPayload(
            **jwt_meta.dict(),
            **jwt_creds.dict(),
        )
        access_token = jwt.encode(token_payload.dict(), secret_key, algorithm=JWT_ALGORITHM)

        return access_token
