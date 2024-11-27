# Build stage
FROM ghcr.io/astral-sh/uv:python3.13-alpine AS build

RUN apk add --no-cache gcc python3-dev musl-dev linux-headers

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
RUN chown -R testuser:testuser /build
RUN mkdir -p /build/reports
RUN chown testuser:testuser /build/reports
USER testuser

# Use the virtual environment's Python for running tests
ENV PATH="/build/.venv/bin:$PATH" \
    PYTHONPATH="/build/src:$PYTHONPATH"

# Run tests with coverage
RUN python -m pytest tests/ \
    --html=/build/reports/pytest.html \
    --self-contained-html \
    --cov=src \
    --cov-report=term \
    --cov-report=html:/build/reports/coverage
RUN cp /build/reports/coverage/index.html /build/reports/coverage.html

# Production Stage
FROM python:3.13-alpine

# Copy from prior stages
COPY --from=test /build/reports /app/reports
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
