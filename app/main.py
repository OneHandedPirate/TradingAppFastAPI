import uuid

from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from app.auth.auth import auth_backend
from app.database.models import User
from app.auth.manager import get_user_manager
from app.auth.schemas import UserRead, UserCreate
from app.routers import operations

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)


app = FastAPI(
    title='Trading App'
)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)


app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(operations.router)
