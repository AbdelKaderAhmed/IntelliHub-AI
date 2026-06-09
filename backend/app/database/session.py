"""
IntelliHub AI - Database Connection Configuration (PostgreSQL Async Engine)
"""
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from app.core.config import settings

# تأمين الرابط برمجياً لضمان احتوائه على مشغل asyncpg غير المتزامن
db_url = settings.DATABASE_URL
if db_url and db_url.startswith("postgresql://"):
    db_url = db_url.replace("postgresql://", "postgresql+asyncpg://", 1)

# بناء المحرك بالرابط المؤمن والمحدث
async_engine = create_async_engine(
    db_url,
    pool_pre_ping=True,
    pool_size=20,
    max_overflow=10,
    future=True
)

AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False
)

async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
    """
    FastAPI Dependency Injector yielding safe scoped asynchronous database sessions.
    Automatically ensures cleanup transactions roll back structural errors.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()