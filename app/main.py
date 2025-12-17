import logging
import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from core.config import settings
from core.helpers import db_helper
from api import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.basicConfig(
        level=settings.log.level,
        format=settings.log.format,
        datefmt=settings.log.datefmt,
    )
    yield

    await db_helper.close_db_engine()


app = FastAPI(lifespan=lifespan)
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
