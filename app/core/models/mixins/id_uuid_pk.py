import uuid
from sqlalchemy.orm import mapped_column, Mapped


class UUIDPkMixin:
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
