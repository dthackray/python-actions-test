# Build stage
FROM ghcr.io/astral-sh/uv:python3.13-alpine AS build

# Change working directory
WORKDIR /build

# Install dependencies first (cached layer)
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-editable

# Copy the project and sync
COPY . .
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-editable

# Test stage
FROM build AS test

# Create non-root test user
RUN adduser -D testuser
USER testuser

# Run tests with coverage
RUN python -m pytest tests/ --cov=src --cov-report=term-missing

# Production Stage
FROM python:3.13-alpine

# Copy only the virtual environment, not the source code
COPY --from=build build/.venv app/.venv

# Create non-root app user
RUN adduser -D appuser
USER appuser

# Set environment
ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app
# Copy application code
COPY --chown=appuser:appuser src/ /app/src/

# Expose port
EXPOSE 8050

# Run the application
CMD ["python", "/app/src/app.py"]
