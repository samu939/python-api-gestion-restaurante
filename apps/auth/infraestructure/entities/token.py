from datetime import datetime, timedelta
from typing import List
from uuid import UUID

from apps.user.infrastructure.db_entity.user_in_db import roleEnum
from config import ACCESS_TOKEN_EXPIRE_MINUTES, JWT_AUDIENCE
from utils.schemas_base import BaseSchema


class JWTMeta(BaseSchema):
    iss: str = "ucab.edu.ve"
    aud: str = JWT_AUDIENCE
    iat: float = datetime.timestamp(datetime.utcnow())
    exp: float = datetime.timestamp(
        datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )


class JWTCreds(BaseSchema):
    """How we'll identify users"""
    username: str


class JWTPayload(JWTMeta, JWTCreds):
    """
    JWT Payload right before it's encoded - combine meta and username
    """

    pass


class AccessToken(BaseSchema):
    access_token: str
    token_type: str


class AuthResponse(AccessToken):
    id: UUID
    name: str
    username: str
    role: roleEnum

