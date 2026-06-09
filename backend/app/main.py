"""
IntelliHub AI - Core System Entrypoint
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.logging import configure_logging
from app.api.v1.analytics.dashboard import router as diagnostic_router

# Initialize system telemetry components
configure_logging()

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    # نتركه افتراضياً ليتمكن الـ Swagger من العثور عليه تلقائياً دون تضارب مع البادئات
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc"
)

# بناء قائمة النطاقات المسموحة مع إضافة سماح شامل للـ Development في Codespaces
development_origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

# دمج النطاقات القادمة من الإعدادات
allowed_origins = [str(origin) for origin in settings.BACKEND_CORS_ORIGINS] + development_origins

# إذا كنا في بيئة تطوير، نفتح الـ CORS بالكامل لكسر قيود المتصفح والـ Codespaces Proxy
if settings.ENVIRONMENT == "development":
    allowed_origins = ["*"]

# Apply explicit security boundary headers via CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True if settings.ENVIRONMENT != "development" or "*" not in allowed_origins else False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root level health indicator endpoint mapping matching primary gateway configuration
@app.get("/", tags=["Gateway Initialization Engine"])
async def root_gateway_handshake() -> dict:
    return {
        # جعلنا المفتاح status قيمته "healthy" ليتوافق مع معايير الـ Load Balancer المستقبلي
        "status": "healthy",
        "message": f"Welcome to {settings.PROJECT_NAME} API Gateway Engine Cluster Interface Layer",
        "docs_url": "/docs"
    }

# Mount modular production feature nodes cleanly
app.include_router(
    diagnostic_router,
    prefix=settings.API_V1_STR,
    tags=["Systems Engineering Operations Diagnostics Control"]
)