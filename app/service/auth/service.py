from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from core.schemas.user import UserCreate, UserRead
from core.models import User
from repository.auth import create_user
from service.security.password import hash_password


async def new_user(user: UserCreate, session: AsyncSession) -> Optional[UserRead]:
    user.password = hash_password(password=user.password)
    user_db = User(**user.model_dump())
    return await create_user(session=session, user=user_db)
