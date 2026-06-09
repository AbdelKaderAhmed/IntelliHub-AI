"""
IntelliHub AI - Clean Architecture Dependency Injector Central Hub
"""
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_async_db
from app.services.storage.s3_service import S3StorageService
from app.services.qdrant.vector_service import VectorStorageService

def get_s3_service() -> S3StorageService:
    return S3StorageService()

def get_vector_service() -> VectorStorageService:
    return VectorStorageService()