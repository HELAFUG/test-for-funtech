from typing import Annotated
from fastapi import APIRouter, Depends, Form
from sqlalchemy.ext.asyncio import AsyncSession
from api.auth.dependencies import get_current_user
from core.schemas.user import UserRead
from core.schemas.order import Order, OrderCreate
from core.helpers import db_helper
from service.order import create_new_order

router = APIRouter(
    dependencies=[Depends(get_current_user)],
)


@router.post("/")
async def order_new(
    order: Annotated[OrderCreate, Form()],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    user: Annotated[UserRead, Depends(get_current_user)],
):
    order = await create_new_order(session=session, order=order, user=user)
    return order
