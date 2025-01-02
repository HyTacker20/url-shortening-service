import re
from datetime import datetime
from typing import Optional
from urllib.parse import urlparse, urlunparse

from pydantic import BaseModel, AnyUrl, ConfigDict, validator, field_validator, Field


class ShortURLCreate(BaseModel):
    url: AnyUrl
    short_code: Optional[str] = Field(None, max_length=50, min_length=6)

    @field_validator("url", mode="before")
    @classmethod
    def validate_url(cls, value):
        url_pattern = "[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b([-a-zA-Z0-9()@:%_\\+.~#?&//=]*)"

        if isinstance(value, str) and re.match(url_pattern, value):
            parsed = urlparse(value)
            if not parsed.scheme:
                value = urlunparse(parsed._replace(scheme="https"))
        return value


class ShortURLResponse(ShortURLCreate):
    id: int
    short_code: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ShortURLWithStatsResponse(ShortURLResponse):
    access_count: int
