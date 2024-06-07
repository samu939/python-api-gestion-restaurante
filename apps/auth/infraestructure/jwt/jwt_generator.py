



from datetime import datetime, timedelta

import jwt
from apps.auth.application.token.token_generator import tokenGenerator
from apps.auth.infraestructure.entities.token import JWTCreds, JWTMeta, JWTPayload
from apps.user.infrastructure.db_entity.user_in_db import UserInDB
from config import ACCESS_TOKEN_EXPIRE_MINUTES, JWT_ALGORITHM, JWT_AUDIENCE, SECRET_KEY


class jwtGenerator (tokenGenerator):
    
    def generate(self, *, user: UserInDB) -> str:
        secret_key: str = str(SECRET_KEY)
        audience: str = JWT_AUDIENCE
        expires_in: int = ACCESS_TOKEN_EXPIRE_MINUTES
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