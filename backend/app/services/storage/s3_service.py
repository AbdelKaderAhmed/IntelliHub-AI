"""
IntelliHub AI - S3 Compatible Enterprise Storage Subsystem
Provides decoupled isolation logic wrappers interacting with MinIO Clusters.
"""
from datetime import timedelta
import io
from typing import BinaryIO, Optional
from minio import Minio
from minio.error import S3Error
import structlog
from app.core.config import settings

logger = structlog.get_logger()

class S3StorageService:
    def __init__(self) -> None:
        # Stripping scheme definitions if present internally in config URL mappings
        endpoint = settings.S3_ENDPOINT_URL.replace("http://", "").replace("https://", "")
        
        self.client = Minio(
            endpoint=endpoint,
            access_key=settings.AWS_ACCESS_KEY_ID,
            secret_key=settings.AWS_SECRET_ACCESS_KEY,
            secure=settings.S3_SECURE
        )
        self._ensure_bucket_exists(settings.S3_BUCKET)

    def _ensure_bucket_exists(self, bucket_name: str) -> None:
        try:
            if not self.client.bucket_exists(bucket_name):
                self.client.make_bucket(bucket_name)
                logger.info("s3_bucket_created", bucket=bucket_name)
        except S3Error as e:
            logger.error("s3_bucket_initialization_failed", error=str(e))
            raise RuntimeError(f"Storage Initialization Error: {e}")

    async def upload_file(
        self, 
        tenant_id: str, 
        file_path: str, 
        file_data: BinaryIO, 
        length: int, 
        content_type: str = "application/octet-stream"
    ) -> str:
        """
        Uploads a raw stream into strict tenant partitioned namespaces.
        Format pattern: storage_root/{tenant_id}/{file_path}
        """
        secured_object_name = f"{tenant_id}/{file_path.lstrip('/')}"
        try:
            self.client.put_object(
                bucket_name=settings.S3_BUCKET,
                object_name=secured_object_name,
                data=file_data,
                length=length,
                content_type=content_type
            )
            logger.info("file_upload_success", tenant_id=tenant_id, target_path=secured_object_name)
            return secured_object_name
        except S3Error as e:
            logger.error("file_upload_failed", tenant_id=tenant_id, error=str(e))
            raise RuntimeError(f"Object Storage Save Failed: {e}")

    async def generate_presigned_download_url(self, object_name: str, expires_minutes: int = 60) -> str:
        """
        Generates direct authenticated URLs to objects bypassing systemic computing constraints.
        """
        try:
            url: str = self.client.get_presigned_url(
                method="GET",
                bucket_name=settings.S3_BUCKET,
                object_name=object_name,
                expires=timedelta(minutes=expires_minutes)
            )
            return url
        except S3Error as e:
            logger.error("url_generation_failed", target_object=object_name, error=str(e))
            raise RuntimeError(f"Failed to generate presigned download mapping: {e}")

    async def delete_file(self, object_name: str) -> None:
        try:
            self.client.remove_object(bucket_name=settings.S3_BUCKET, object_name=object_name)
            logger.info("file_deletion_success", target_object=object_name)
        except S3Error as e:
            logger.error("file_deletion_failed", target_object=object_name, error=str(e))
            raise RuntimeError(f"Failed execution on removing remote file context: {e}")