"""
IntelliHub AI - Deep System Diagnostic Engineering Health Gateway
"""
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text
import structlog
from app.database.session import get_async_db
from app.core.dependencies import get_s3_service, get_vector_service
from app.services.storage.s3_service import S3StorageService
from app.services.qdrant.vector_service import VectorStorageService

logger = structlog.get_logger()
router = APIRouter()

@router.get("/health", status_code=status.HTTP_200_OK)
async def system_deep_diagnostic_health_check(
    db: AsyncSession = Depends(get_async_db),
    s3: S3StorageService = Depends(get_s3_service),
    vector_db: VectorStorageService = Depends(get_vector_service)
) -> dict:
    """
    Executes an all-encompassing active diagnostic health check against downstream enterprise components.
    """
    postgres_status = "unhealthy"
    s3_status = "unhealthy"
    vector_status = "unhealthy"

    # 1. Evaluate Relational Transaction Pipeline
    try:
        await db.execute(text("SELECT 1"))
        postgres_status = "healthy"
    except Exception as e:
        logger.error("health_check_postgres_failed", error=str(e))

    # 2. Evaluate Object Storage Target Cluster Connectivity
    try:
        from app.core.config import settings
        s3.client.bucket_exists(settings.S3_BUCKET)
        s3_status = "healthy"
    except Exception as e:
        logger.error("health_check_s3_failed", error=str(e))

    # 3. Evaluate Vector Cluster Heartbeats
    try:
        await vector_db.client.get_collections()
        vector_status = "healthy"
    except Exception as e:
        logger.error("health_check_qdrant_failed", error=str(e))

    # Overall system compilation assessment
    overall_status = "online"
    if "unhealthy" in [postgres_status, s3_status, vector_status]:
        overall_status = "degraded"

    return {
        "status": overall_status,
        "services": {
            "relational_db_postgres": postgres_status,
            "object_storage_minio": s3_status,
            "vector_db_qdrant": vector_status
        }
    }