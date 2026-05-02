FROM python:3.14.4-slim-trixie

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml ./pyproject.toml

COPY uv.lock ./uv.lock

COPY backend /app

RUN uv sync --locked

