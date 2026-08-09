FROM python:3.12-slim

# Copy uv/uvx binaries from the official astral image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Copy dependency files first (for layer caching)
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen

# Copy the rest of the project
COPY . .

ENV PATH="/app/.venv/bin:$PATH"

CMD ["uv", "run", "python", "-m", "server"]
