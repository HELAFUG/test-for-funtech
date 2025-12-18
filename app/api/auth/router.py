from typing import Optional, Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, HTTPException, Depends
from service.auth import new_user
from core.schemas.user import UserCreate, UserRead
from core.helpers import db_helper

router = APIRouter()


@router.post("/register", response_model=UserRead)
async def register_new_user(
    user_schema: UserCreate,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> Optional[UserRead]:
    user = await new_user(session=session, user=user_schema)
    if user:
        return user

    raise HTTPException(status_code=400, detail="User already exists")
