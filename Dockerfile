# syntax=docker/dockerfile:1

FROM --platform=linux/amd64 python:3.10-slim

ENV PIP_NO_CACHE_DIR=false \
    POETRY_VIRTUALENVS_CREATE=false

# Install Poetry
RUN pip3 install -U poetry

# Create working directory
RUN mkdir -p /usr/src/squiddie
WORKDIR /usr/src/squiddie

# Install dependencies
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev

COPY . .

ENTRYPOINT ["python3"]
CMD ["-m", "squiddie"]
