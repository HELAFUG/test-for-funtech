from typing import Annotated
from fastapi.security.oauth2 import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from service.jwt.token import decode_token
from repository.auth import get_user
from core.helpers import db_helper
from core.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=settings.api.token_url)


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    payload = decode_token(token)
    username: str = payload.get("sub")
    if username is None:
        raise credentials_exception

    user = await get_user(username=username, session=session)
    if user is None:
        raise credentials_exception
    return user
