FROM python:3.13-bookworm

# Install system dependencies, Rust, and maturin
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y \
    && export PATH="$HOME/.cargo/bin:$PATH" \
    && rm -rf /var/lib/apt/lists/*

# Ensure Rust is in PATH for all subsequent RUN commands
ENV PATH="/root/.cargo/bin:$PATH"

# Upgrade pip and setuptools
RUN python -m pip install --upgrade pip setuptools

# Install maturin
RUN pip install maturin

# Set up the working directory
RUN mkdir "backend"
WORKDIR /backend

COPY ./poetry.lock ./pyproject.toml ./

RUN pip install poetry

RUN pip install pendulum==3.0.0 --no-build-isolation
RUN poetry config virtualenvs.create false

# Install project dependencies
RUN poetry install --no-root --only main

# Copy application code
COPY ./src ./src

# Command to start the FastAPI server
CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]