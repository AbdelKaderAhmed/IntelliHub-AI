# IntelliHub AI(AI Knowledge Hub for SMEs)

Enterprise AI Knowledge Platform powered by Retrieval-Augmented Generation (RAG)

## Overview

AI Knowledge Hub for SMEs is a multi-tenant enterprise knowledge management platform that enables organizations to transform internal documents into a searchable AI-powered knowledge assistant.

The platform allows employees to upload documents, search organizational knowledge, ask questions in natural language, and receive accurate answers supported by citations.

Built with modern AI infrastructure including FastAPI, Next.js, Groq LLMs, Qdrant Vector Database, PostgreSQL, and S3-compatible storage.

---

# Core Features

## Knowledge Management

* Document Upload
* Document Versioning
* Metadata Extraction
* OCR Processing
* Citation Tracking

## AI Search

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Hybrid Search
* Reranking
* Source Attribution

## Enterprise Features

* Multi-Tenant Architecture
* JWT Authentication
* Role-Based Access Control
* Audit Logging
* Analytics Dashboard

## Supported Languages

* Arabic
* French
* English

---

# Technology Stack

## Frontend

* Next.js 15
* React 19
* TypeScript
* Tailwind CSS
* Shadcn UI
* TanStack Query

## Backend

* FastAPI
* Python 3.12+
* Pydantic
* SQLAlchemy

## AI Layer

* Groq API
* Llama 3.3 70B Versatile
* multilingual-e5-large
* LangChain
* LangGraph

## Vector Database

* Qdrant

## Relational Database

* PostgreSQL

## Authentication

* JWT
* Refresh Tokens
* RBAC

## Storage

* MinIO
* Amazon S3 Compatible Storage

## DevOps

* Docker
* Docker Compose
* GitHub Actions
* Nginx

---

# System Architecture

User

↓

Next.js Frontend

↓

FastAPI Backend

↓

Authentication Layer

↓

Knowledge Service

↓

Retriever

↓

Qdrant Vector Database

↓

Groq Llama 3.3 70B

↓

Answer + Citations

---

# Folder Structure

```text
ai-knowledge-hub/

├── backend/
│
│   ├── app/
│   │
│   │   ├── api/
│   │   │
│   │   │   ├── v1/
│   │   │   │
│   │   │   ├── auth/
│   │   │   │   ├── login.py
│   │   │   │   ├── register.py
│   │   │   │   └── refresh.py
│   │   │   │
│   │   │   ├── documents/
│   │   │   │   ├── upload.py
│   │   │   │   ├── delete.py
│   │   │   │   ├── update.py
│   │   │   │   └── metadata.py
│   │   │   │
│   │   │   ├── chat/
│   │   │   │   ├── ask.py
│   │   │   │   ├── history.py
│   │   │   │   └── citations.py
│   │   │   │
│   │   │   └── analytics/
│   │   │       └── dashboard.py
│   │
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── security.py
│   │   │   ├── logging.py
│   │   │   └── dependencies.py
│   │
│   │   ├── database/
│   │   │   ├── session.py
│   │   │   ├── base.py
│   │   │   └── migrations/
│   │
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── tenant.py
│   │   │   ├── document.py
│   │   │   ├── conversation.py
│   │   │   └── audit_log.py
│   │
│   │   ├── schemas/
│   │   │   ├── auth.py
│   │   │   ├── document.py
│   │   │   ├── chat.py
│   │   │   └── analytics.py
│   │
│   │   ├── services/
│   │   │
│   │   │   ├── auth/
│   │   │   │   ├── jwt_service.py
│   │   │   │   └── password_service.py
│   │   │
│   │   │   ├── storage/
│   │   │   │   └── s3_service.py
│   │   │
│   │   │   ├── qdrant/
│   │   │   │   └── vector_service.py
│   │   │
│   │   │   ├── embeddings/
│   │   │   │   └── embedding_service.py
│   │   │
│   │   │   ├── llm/
│   │   │   │   └── groq_service.py
│   │   │
│   │   │   └── analytics/
│   │   │       └── analytics_service.py
│   │
│   │   ├── rag/
│   │   │
│   │   │   ├── ingestion/
│   │   │   │   ├── pipeline.py
│   │   │   │   ├── chunking.py
│   │   │   │   └── metadata.py
│   │   │
│   │   │   ├── loaders/
│   │   │   │   ├── pdf_loader.py
│   │   │   │   ├── docx_loader.py
│   │   │   │   ├── xlsx_loader.py
│   │   │   │   ├── txt_loader.py
│   │   │   │   └── ocr_loader.py
│   │   │
│   │   │   ├── retrieval/
│   │   │   │   ├── retriever.py
│   │   │   │   ├── hybrid_search.py
│   │   │   │   └── reranker.py
│   │   │
│   │   │   ├── chains/
│   │   │   │   ├── qa_chain.py
│   │   │   │   └── summary_chain.py
│   │   │
│   │   │   └── prompts/
│   │   │       ├── qa_prompt.py
│   │   │       └── summary_prompt.py
│   │
│   │   └── main.py
│   │
│   ├── tests/
│   │   ├── test_auth.py
│   │   ├── test_upload.py
│   │   ├── test_rag.py
│   │   └── test_chat.py
│   │
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
│
├── frontend/
│
│   ├── src/
│   │
│   │   ├── app/
│   │   │
│   │   ├── (auth)/
│   │   │   ├── login/
│   │   │   └── register/
│   │   │
│   │   ├── dashboard/
│   │   │
│   │   ├── documents/
│   │   │
│   │   ├── chat/
│   │   │
│   │   └── analytics/
│   │
│   │   ├── components/
│   │   │   ├── chat/
│   │   │   ├── upload/
│   │   │   ├── citations/
│   │   │   ├── dashboard/
│   │   │   └── shared/
│   │
│   │   ├── hooks/
│   │   ├── services/
│   │   ├── types/
│   │   ├── lib/
│   │   └── store/
│   │
│   ├── public/
│   ├── Dockerfile
│   └── package.json
│
├── infrastructure/
│
│   ├── docker/
│   │   ├── backend.Dockerfile
│   │   ├── frontend.Dockerfile
│   │   └── nginx.Dockerfile
│   │
│   ├── nginx/
│   │   └── nginx.conf
│   │
│   └── compose/
│       └── docker-compose.yml
│
├── storage/
│   ├── uploads/
│   ├── processed/
│   └── temp/
│
├── docs/
│   ├── architecture.md
│   ├── api-reference.md
│   ├── deployment.md
│   └── roadmap.md
│
├── .github/
│   └── workflows/
│       ├── backend.yml
│       └── frontend.yml
│
├── README.md
├── LICENSE
└── .gitignore
```

---

# Development Roadmap

## Phase 1

* Authentication
* Document Upload
* PDF Processing
* Basic RAG

## Phase 2

* Multi-Format Support
* Qdrant Integration
* Citations

## Phase 3

* Multi-Tenant Architecture
* RBAC
* Analytics Dashboard

## Phase 4

* Hybrid Search
* Reranking
* OCR

## Phase 5

* Agentic Workflows
* Knowledge Insights
* Automated Reports

---

# Production Goals

* Enterprise Security
* Horizontal Scalability
* Low Latency Retrieval
* Multilingual Search
* Explainable AI Answers
* Auditability
* SaaS Ready Architecture
