from typing import Optional
from datetime import datetime, timedelta
from sqlalchemy.ext.asyncio import AsyncSession
from core.schemas.user import UserCreate, UserRead
from core.schemas.access_token import AccessToken
from core.models import User
from repository.auth import create_user, get_user
from service.security.password import hash_password, verify_password
from service.jwt.token import encode_token


async def new_user(user: UserCreate, session: AsyncSession) -> Optional[UserRead]:
    user.password = hash_password(password=user.password)
    user_db = User(**user.model_dump())
    return await create_user(session=session, user=user_db)


async def get_exist_user(
    username: str, password: str, session: AsyncSession
) -> Optional[AccessToken]:
    user = await get_user(session=session, username=username)
    decrypt_result = verify_password(password=password, hashed_password=user.password)

    if user and decrypt_result:
        token = encode_token(
            payload={
                "sub": user.username,
                "exp": datetime.utcnow() + timedelta(minutes=30),
                "iat": datetime.utcnow(),
            }
        )
        return AccessToken(access_token=token, token_type="bearer")

    return None
