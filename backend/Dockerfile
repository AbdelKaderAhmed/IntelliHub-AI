# Use official lightweight Python image
FROM python:3.12-slim AS base

# Set environment variables to optimize Python execution within Docker
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# Set system working directory
WORKDIR /app

# Install critical system dependencies required for building wheels and OCR utilities later
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency definition file to leverage Docker layer caching
COPY requirements.txt .

# Install explicit python packages defined in requirements
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the rest of the application codebase
COPY . .

# Expose the internal network port for FastAPI
EXPOSE 8000

# Run FastAPI application via production server Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]