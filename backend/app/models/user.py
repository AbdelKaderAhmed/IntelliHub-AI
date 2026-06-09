"""
IntelliHub AI - User Identity Domain Model
"""
import enum
from typing import TYPE_CHECKING
from uuid import UUID, uuid4
from sqlalchemy import String, ForeignKey, Enum, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base import Base, TimeStampedModel

if TYPE_CHECKING:
    from app.models.tenant import Tenant

class UserRole(str, enum.Enum):
    """
    System RBAC security matrix roles mapping explicitly to corporate structure.
    """
    SUPER_ADMIN = "super_admin"  # Platform operator level
    TENANT_ADMIN = "tenant_admin" # SME Administrator level
    POWER_USER = "power_user"     # Standard engineering/legal officer with write permissions
    READ_ONLY = "read_only"       # View-only access level for specific documents


class User(Base, TimeStampedModel):
    """
    Represents an authenticated individual belonging to a specific isolated tenant partition.
    """
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4, index=True)
    tenant_id: Mapped[UUID] = mapped_column(
        ForeignKey("tenants.id", ondelete="CASCADE"), 
        nullable=False, 
        index=True
    )
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole, name="user_role_enum", native_enum=True),
        default=UserRole.READ_ONLY,
        nullable=False
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    # Relationships
    tenant: Mapped["Tenant"] = relationship("Tenant", back_populates="users", lazy="raise")

    def __repr__(self) -> str:
        return f"<User(id={self.id}, email='{self.email}', role='{self.role.value}')>"