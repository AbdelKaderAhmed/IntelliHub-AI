"""
IntelliHub AI - Tenant Data Domain Model
"""
from typing import List, TYPE_CHECKING
from uuid import UUID, uuid4
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base import Base, TimeStampedModel

if TYPE_CHECKING:
    from app.models.user import User

class Tenant(Base, TimeStampedModel):
    """
    Represents an isolated organizational entity (SME, Law Firm, NGO, etc.)
    within the IntelliHub multi-tenant ecosystem.
    """
    __tablename__ = "tenants"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    slug: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    # Relationships (Cascades ensure that removing a tenant safely evicts its user cluster)
    users: Mapped[List["User"]] = relationship(
        "User",
        back_populates="tenant",
        cascade="all, delete-orphan",
        lazy="raise"
    )

    def __repr__(self) -> str:
        return f"<Tenant(id={self.id}, name='{self.name}', slug='{self.slug}')>"