from fastapi import APIRouter
from .router import router

auth_router = APIRouter(tags=["Auth"])
auth_router.include_router(router)
