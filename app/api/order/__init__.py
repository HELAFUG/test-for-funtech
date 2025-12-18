from fastapi import APIRouter
from .router import router

order_router = APIRouter(prefix="/orders", tags=["Order"])
order_router.include_router(router)
