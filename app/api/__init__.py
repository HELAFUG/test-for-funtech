from fastapi import APIRouter
from core.config import settings
from api.auth import auth_router
from api.order import order_router

router = APIRouter(
    prefix=settings.api.prefix,
    responses={404: {"description": "Not found"}},
)

router.include_router(auth_router)
router.include_router(order_router)
