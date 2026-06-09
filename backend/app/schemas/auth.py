"""
IntelliHub AI - Data Transfer Objects & Validation Schemas
"""
from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field, ConfigDict
from app.models.user import UserRole

# ==========================================
# Tenant Validation Schemas
# ==========================================
class TenantBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=255, description="Corporate name of the SME")
    slug: str = Field(..., min_length=2, max_length=255, description="URL-friendly identifier unique to tenant")

class TenantCreate(TenantBase):
    pass

class TenantResponse(TenantBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: UUID
    is_active: bool
    created_at: datetime

# ==========================================
# User Validation Schemas
# ==========================================
class UserBase(BaseModel):
    email: EmailStr = Field(..., description="Corporate identity email mapping")
    role: UserRole = Field(default=UserRole.READ_ONLY, description="Assigned RBAC Authorization Level")

class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=128, description="Plaintext password to be processed securely")
    tenant_id: UUID = Field(..., description="Target parent isolation node identifier")

class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: UUID
    tenant_id: UUID
    is_active: bool
    created_at: datetime