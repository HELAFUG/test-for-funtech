from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.models import Order


async def create_order(
    session: AsyncSession, order: Order, user_id: int
) -> Optional[Order]:
    session.add(order)
    await session.commit()
    return order


async def get_order(session: AsyncSession, order_id: int) -> Optional[Order]:
    result = await session.execute(select(Order).where(Order.id == order_id))
    return result.scalars().first()


async def get_all_orders(session: AsyncSession, user_id: int) -> list[Order]:
    result = await session.execute(select(Order).where(Order.user_id == user_id))
    return result.scalars().all()


async def update_order(session: AsyncSession, order: Order) -> Optional[Order]:
    session.add(order)
    await session.commit()
    await session.refresh(order)
    return order


async def delete_order(session: AsyncSession, order_id: int) -> None:
    order = await get_order(session=session, order_id=order_id)
    await session.delete(order)
    await session.commit()
