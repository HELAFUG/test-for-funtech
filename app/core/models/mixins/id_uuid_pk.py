import uuid
from sqlalchemy import UUID
from sqlalchemy.orm import mapped_column, Mapped


class UUIDPkMixin:
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
