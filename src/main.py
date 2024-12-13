from fastapi import FastAPI

from db.base import init_models
from endpoints.short_urls import router_url_shortener


def get_application() -> FastAPI:
    _app = FastAPI(title="URL Shortener")

    @_app.on_event("startup")
    async def startup():
        await init_models()

    _app.include_router(router_url_shortener, prefix="/shorten", tags=["url_shortener"])

    return _app


app = get_application()
