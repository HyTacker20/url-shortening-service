from datetime import datetime, UTC

from sqlalchemy import Column, Integer, String, DateTime

from db.base import Base


class ShortURL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, index=True)
    url = Column(String)
    short_code = Column(String, index=True, unique=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now(UTC))
    updated_at = Column(DateTime(timezone=True), default=datetime.now(UTC), onupdate=datetime.now(UTC))
    access_count = Column(Integer, default=0)
