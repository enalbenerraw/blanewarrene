from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Text, DateTime
from datetime import datetime, timezone
import uuid

from app.config import get_settings


class Base(DeclarativeBase):
    pass


class Briefing(Base):
    __tablename__ = "briefings"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id: Mapped[str] = mapped_column(String, index=True)
    company_name: Mapped[str] = mapped_column(String)
    company_url: Mapped[str] = mapped_column(String)
    time_period: Mapped[str] = mapped_column(String, default="6 months")
    status: Mapped[str] = mapped_column(String, default="pending")
    content: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )


engine = create_async_engine(get_settings().database_url)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
