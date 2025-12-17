from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from core.config import settings


class DataBaseHelper:
    def __init__(self, url: str, echo: bool) -> None:
        self.engine = create_async_engine(url=url, echo=echo)

        self.session_factory = async_sessionmaker(
            bind=self.engine, expire_on_commit=False, autoflush=False, autocommit=False
        )

    async def dispose(self):
        await self.engine.dispose()

    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session


db_helper = DataBaseHelper(url=settings.db.url, echo=settings.db.echo)
