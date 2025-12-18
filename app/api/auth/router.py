from typing import Optional, Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from service.auth import new_user, get_exist_user
from core.schemas.user import UserCreate, UserRead
from core.schemas.access_token import AccessToken
from core.helpers import db_helper
from api.auth.dependencies import get_current_user

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


@router.post("/token", response_model=AccessToken)
async def login_exist_user(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    token = await get_exist_user(
        session=session,
        username=form_data.username,
        password=form_data.password,
    )

    if token:
        return token

    raise HTTPException(status_code=400, detail="Incorrect username or password")


@router.get("/me", response_model=UserRead)
async def read_users_me(current_user: Annotated[UserRead, Depends(get_current_user)]):
    return current_user
