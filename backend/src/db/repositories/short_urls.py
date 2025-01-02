import random

from fastapi import HTTPException
from fastapi.responses import Response
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.db.models.short_urls import ShortURL
from src.schemas.short_urls import ShortURLCreate, ShortURLWithStatsResponse, ShortURLResponse
from src.utils.url_shortener import generate_short_code


class ShortURLService:
    def __init__(self):
        self.model = ShortURL

    async def create(self, new_object: ShortURLCreate, db: AsyncSession) -> ShortURL:
        object_dict = new_object.model_dump()
        print(object_dict)
        object_dict["url"] = str(new_object.url)
        if not new_object.short_code:
            object_dict["short_code"] = generate_short_code(new_object.url)

        instance = self.model(**object_dict)
        db.add(instance)

        try:
            await db.commit()
            await db.refresh(instance)
        except Exception as e:
            await db.rollback()
            raise e

        return instance

    async def get(self, short_code: str,
                  db: AsyncSession,
                  with_stats=False) \
            -> ShortURLResponse | ShortURLWithStatsResponse:
        query = select(self.model).where(self.model.short_code == short_code)
        db_object = await db.execute(query)
        instance: ShortURL = db_object.scalar()

        if not instance:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="This URL was not found!"
            )

        if not with_stats:
            await self._update_stats(instance, db)

        print(instance.url)
        print(instance.access_count)

        return instance

    @staticmethod
    async def _update_stats(url_instance: ShortURL, db: AsyncSession):
        try:
            url_instance.access_count += 1
            await db.commit()
        except Exception as e:
            print(f"Failed to update stats: {e}")
            await db.rollback()

    async def update(self, short_code: str,
                     updated_object: ShortURLCreate,
                     db: AsyncSession) -> ShortURL:
        async with db.begin():
            query = update(self.model).where(self.model.short_code == short_code).values(url=str(updated_object.url))
            await db.execute(query)

        result = await db.execute(select(self.model).filter(self.model.short_code == short_code))
        updated_instance = result.scalar_one()
        return updated_instance

    async def delete(self, short_code: str, db: AsyncSession) -> Response:
        result = await db.execute(select(self.model).filter(self.model.short_code == short_code))
        instance = result.scalar()

        if not instance:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="This URL was not found!"
            )

        await db.delete(instance)
        await db.commit()

        return Response(status_code=status.HTTP_204_NO_CONTENT)


def get_short_url_service() -> ShortURLService:
    return ShortURLService()
