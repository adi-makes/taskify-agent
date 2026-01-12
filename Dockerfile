# Taskify Agent - Production Dockerfile
# Multi-stage build for optimized image size

# ═══════════════════════════════════════════════
# Stage 1: Builder
# ═══════════════════════════════════════════════
FROM python:3.11-slim as builder

WORKDIR /build

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# ═══════════════════════════════════════════════
# Stage 2: Runtime
# ═══════════════════════════════════════════════
FROM python:3.11-slim

# Create non-root user for security
RUN useradd -m -u 1000 taskify && \
    mkdir -p /app && \
    chown -R taskify:taskify /app

WORKDIR /app

# Copy Python dependencies from builder
COPY --from=builder /root/.local /home/taskify/.local

# Copy application code
COPY --chown=taskify:taskify agent.py config.py ./
COPY --chown=taskify:taskify tools/ ./tools/
COPY --chown=taskify:taskify examples/ ./examples/

# Set environment variables
ENV PATH=/home/taskify/.local/bin:$PATH \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Switch to non-root user
USER taskify

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "from config import Config; Config.validate()" || exit 1

# Default command
CMD ["python", "agent.py"]
