import jwt
from core.config import settings


def encode_token(payload: dict) -> str:
    return jwt.encode(
        payload, settings.auth.secret_key, algorithm=settings.auth.algorithm
    )


def decode_token(token: str) -> dict:
    return jwt.decode(
        token, settings.auth.secret_key, algorithms=[settings.auth.algorithm]
    )
