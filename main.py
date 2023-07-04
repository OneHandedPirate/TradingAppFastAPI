import uuid

from fastapi import FastAPI, Request, status
from fastapi.exceptions import ValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi_users import fastapi_users, FastAPIUsers

from auth.auth import auth_backend
from database.models import User
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate


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
