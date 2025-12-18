from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from core.schemas.order import OrderCreate, Order
from core.models import User, Order
from repository.order import create_order, get_order, get_all_orders, delete_order


async def create_new_order(
    session: AsyncSession,
    order: OrderCreate,
    user: User,
) -> Optional[Order]:
    order_db = Order(user_id=user.id, items=order.items)
    order = await create_order(
        session=session,
        order=order_db,
        user_id=user.id,
    )
    return order
