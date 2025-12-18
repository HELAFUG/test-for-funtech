from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.models.mixins import IdIntPkMixin
from core.models import Base

if TYPE_CHECKING:
    from core.models import Order


class User(Base, IdIntPkMixin):
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    orders: Mapped[list["Order"]] = relationship(back_populates="user")
