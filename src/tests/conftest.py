import asyncio
import os

import pytest
import pytest_asyncio
from fastapi import FastAPI
from httpx import AsyncClient
from pydantic import AnyUrl

from src.db.base import async_session, engine, Base
from src.db.models.short_urls import ShortURL
from src.utils.url_shortener import generate_short_code

os.environ["TESTING"] = "True"  # Env variable for switching to test db connection


# Open event loop for async test session
@pytest.fixture(autouse=True, scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(autouse=True, scope="module")
def app() -> FastAPI:
    from main import get_application  # local import for testing purpose

    app = get_application()
    return app


# Creation and drop tables for each test (isolation)
@pytest_asyncio.fixture(autouse=True)
async def db_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture
async def session():
    session = async_session()
    yield session


@pytest.fixture
async def create_short_url(session) -> ShortURL:
    url = AnyUrl("https://www.test.com")
    db_obj = ShortURL(
        url=str(url),
        short_code=generate_short_code(url)
    )
    session.add(db_obj)
    await session.commit()
    return db_obj


@pytest.fixture
async def client(app: FastAPI) -> AsyncClient:
    async with AsyncClient(
            app=app,
            base_url="http://localhost",
    ) as client:
        yield client
