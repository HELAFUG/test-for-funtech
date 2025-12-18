from typing import List
from pydantic import BaseModel
from internal_types.order_types import OrderStatus


class OrderBase(BaseModel):
    items: List[str]


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    user_id: int
    id: int
    status: OrderStatus
    created_at: str


class OrderUpdate(BaseModel):
    status: OrderStatus
