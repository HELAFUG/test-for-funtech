from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.models import User


async def get_user(session: AsyncSession, username: str) -> Optional[User]:
    result = await session.execute(select(User).where(User.username == username))
    return result.scalars().first()


async def create_user(session: AsyncSession, user: User) -> Optional[User]:
    user_exist = await get_user(session, user.username)

    if user_exist:
        return None

    session.add(user)
    await session.commit()
    return user
