from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from core.schemas.order import OrderCreate, OrderRead
from core.models import User
from repository.order import create_order, get_order, get_all_orders, delete_order


async def create_new_order(
    session: AsyncSession, order: OrderCreate, user: User
) -> Optional[OrderRead]:
    order = await create_order(
        session=session,
        order=order,
        user_id=user.id,
    )
    return order
