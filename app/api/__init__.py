from fastapi import APIRouter
from core.config import settings

router = APIRouter(
    prefix=settings.api.prefix,
    responses={404: {"description": "Not found"}},
)
