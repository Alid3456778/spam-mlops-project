# syntax=docker/dockerfile:1
FROM python:3.10-slim

# Keep Python lean and logs unbuffered
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Install only runtime dependencies required by api/app.py
# (mlflow and pandas removed to reduce image size)
RUN pip install --no-cache-dir fastapi uvicorn scikit-learn numpy python-dotenv requests

# Copy only what the API needs at runtime
COPY api/ /app/api/
COPY models/ /app/models/

EXPOSE 8000

CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]
