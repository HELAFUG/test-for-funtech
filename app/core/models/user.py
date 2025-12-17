from sqlalchemy.orm import Mapped, mapped_column
from core.models.mixins import IdIntPkMixin
from core.models import Base


class User(Base, IdIntPkMixin):
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
