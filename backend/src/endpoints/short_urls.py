from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.repositories.short_urls import ShortURLService, get_short_url_service
from src.schemas.short_urls import ShortURLResponse, ShortURLCreate, ShortURLWithStatsResponse

from src.db.base import get_session

router_url_shortener = APIRouter()


@router_url_shortener.post("/", response_model=ShortURLResponse)
async def create_url(
        new_object: ShortURLCreate,
        url_shortener_service: ShortURLService = Depends(get_short_url_service),
        db: AsyncSession = Depends(get_session),
):
    return await url_shortener_service.create(new_object, db)

@router_url_shortener.get("/{short_code}", response_model=ShortURLResponse)
@cache(expire=60)
async def get_url(
        short_code: str,
        url_shortener_service: ShortURLService = Depends(get_short_url_service),
        db: AsyncSession = Depends(get_session),
):
    return await url_shortener_service.get(short_code, db)


@router_url_shortener.put("/{short_code}", response_model=ShortURLResponse)
async def update_url(
        short_code: str,
        updated_object: ShortURLCreate,
        url_shortener_service: ShortURLService = Depends(get_short_url_service),
        db: AsyncSession = Depends(get_session),
):
    return await url_shortener_service.update(short_code, updated_object, db)


@router_url_shortener.delete("/{short_code}")
async def delete_url(
        short_code: str,
        url_shortener_service: ShortURLService = Depends(get_short_url_service),
        db: AsyncSession = Depends(get_session)
):
    return await url_shortener_service.delete(short_code, db)


@router_url_shortener.get("/{short_code}/stats", response_model=ShortURLWithStatsResponse)
async def get_url_with_stats(
        short_code: str,
        url_shortener_service: ShortURLService = Depends(get_short_url_service),
        db: AsyncSession = Depends(get_session)
):
    return await url_shortener_service.get(short_code, db, with_stats=True)
