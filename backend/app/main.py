from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="IntelliHub AI - Enterprise Knowledge Platform",
    description="RAG-powered multi-tenant knowledge management system for SMEs.",
    version="1.0.0"
)

# إعدادات الـ CORS للسماح لـ Next.js بالاتصال بالسيرفر
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # رابط فرونت اند Next.js
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "status": "online",
        "message": "Welcome to IntelliHub AI API Gateway",
        "docs_url": "/docs"
    }