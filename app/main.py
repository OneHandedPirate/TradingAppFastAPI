from fastapi import FastAPI
from redis import asyncio as aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi.middleware.cors import CORSMiddleware

from app.auth.auth import auth_backend, fastapi_users_users
from app.auth.schemas import UserRead, UserCreate
from app.routers.operations import router as operations_router
from app.routers.tasks import router as tasks_router
from environ import REDIS_PORT, REDIS_HOST


app = FastAPI(
    title='Trading App'
)


app.include_router(
    fastapi_users_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)


app.include_router(
    fastapi_users_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(operations_router)
app.include_router(tasks_router)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(f"redis://{REDIS_HOST}:{REDIS_PORT}")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],   # На проде обязательно нужно указывать все методы
    allow_headers=["*"],   # и заголовки
)