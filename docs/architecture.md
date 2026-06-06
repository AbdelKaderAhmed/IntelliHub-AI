Architecture

High-Level Flow

User
↓
Next.js Frontend
↓
FastAPI API
↓
Authentication Layer
↓
Knowledge Service
↓
Retriever
↓
Qdrant
↓
Groq LLM
↓
Answer + Citations

RAG Pipeline

Document Upload
↓
Text Extraction
↓
Chunking
↓
Embedding
↓
Qdrant Indexing
↓
Retriever
↓
Reranking
↓
Groq
↓
Answer

Multi-Tenant Model

Tenant
├── Users
├── Documents
├── Chats
└── Knowledge Base
Each tenant has complete data isolation.

Security Principles

JWT Authentication

Password Hashing

Tenant Isolation

Role-Based Access Control

Audit Logging
