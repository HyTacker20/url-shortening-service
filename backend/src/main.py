from contextlib import asynccontextmanager

import redis
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from starlette.middleware.cors import CORSMiddleware

from .db.base import init_models
from fastapi_cache.backends.redis import RedisBackend
from src.endpoints.short_urls import router_url_shortener


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis_client = redis.asyncio.from_url("redis://redis-cache:6379")
    FastAPICache.init(RedisBackend(redis_client), prefix="fastapi-cache")
    await init_models()
    yield


def get_application() -> FastAPI:
    _app = FastAPI(title="URL Shortener", lifespan=lifespan)
    _app.include_router(router_url_shortener, prefix="/shorten", tags=["url_shortener"])

    origins = [
        "http://localhost:3000",
        "localhost:3000"
    ]

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    @_app.get("/")
    def read_root():
        return {"message": "Hello, World!"}

    return _app


app = get_application()
