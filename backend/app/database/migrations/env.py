"""
IntelliHub AI - Alembic Migration Environment Configuration
Operates cleanly over Asyncpg / SQLAlchemy 2.0 architecture boundaries.
"""
import asyncio
from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy.ext.asyncio import create_async_engine

from alembic import context

# جلب إعدادات المنظومة ونواة الجداول الأساسية
from app.core.config import settings
from app.database.base import Base

# This is the Alembic Config object
config = context.config

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ربط كاشف التغيرات الهيكلية بنواة الموديلات الموحدة لـ IntelliHub
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = settings.DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    """Execution helper boundary running inside the synchronous context runner."""
    context.configure(
        connection=connection, 
        target_metadata=target_metadata
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Run migrations in 'online' mode using a clean direct Async Engine."""
    
    # بناء المحرك بشكل مباشر تماماً لتجنب الـ KeyError الخاص بـ async_engine_from_config
    connectable = create_async_engine(
        settings.DATABASE_URL,
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        # تنفيذ الترحيل بطريقة متوافقة مع الـ Context الخاص بـ Alembic
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


def run_async_migrations() -> None:
    """Handles orchestration boundary between sync invocation and async execution."""
    if context.is_offline_mode():
        run_migrations_offline()
    else:
        # حماية البيئة من تضارب الـ Running Loops في بيئات التطوير الحية
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = None

        if loop and loop.is_running():
            # إذا كان الـ Loop نشطاً، ننتظر تنفيذ الدالة بشكل مباشر ومتزامن داخل البيئة السحابية
            # نستخدم دالة التضمين المباشرة لـ Alembic لضمان عدم التعليق
            loop.run_until_complete(run_migrations_online())
        else:
            asyncio.run(run_migrations_online())


# بدء تشغيل الهجرة الهيكلية بأمان
if __name__ == "__main__" or True:
    run_async_migrations()