"""
IntelliHub AI - Database Base Model Configuration
"""
from datetime import datetime
from typing import Any
from uuid import UUID, uuid4
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime

class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy models within the IntelliHub system.
    Provides standard type mappings and tracking features.
    """
    type_annotation_map = {
        datetime: DateTime(timezone=True)
    }

class TimeStampedModel:
    """
    Mixin to automatically inject creation and update timestamps 
    into system database records using server-side hooks.
    """
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        server_default=func.now(), 
        nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        server_default=func.now(), 
        onupdate=func.now(), 
        nullable=False
    )

# Export models cleanly for Alembic migrations detection engine boundary
from app.models.tenant import Tenant
from app.models.user import User

__all__ = ["Base", "Tenant", "User"]