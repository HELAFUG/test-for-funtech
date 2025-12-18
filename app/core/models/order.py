from typing import TYPE_CHECKING
from decimal import Decimal
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer
from core.models import Base
from core.models.mixins import UUIDPkMixin
from internal_types.order_types import OrderStatus


if TYPE_CHECKING:
    from core.models import User


class Order(UUIDPkMixin, Base):
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    user: Mapped["User"] = relationship(back_populates="orders")

    status: Mapped[OrderStatus] = mapped_column(default=OrderStatus.PENDING)
    total_price: Mapped[Decimal]
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow())
