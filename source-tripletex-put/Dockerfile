# -------- Base image with Python --------
FROM python:3.9.11-alpine3.15 as base

# -------- Build stage: install dependencies --------
FROM base as builder
WORKDIR /airbyte/integration_code

# Upgrade pip and install build deps
RUN apk --no-cache upgrade \
    && pip install --upgrade pip \
    && apk --no-cache add tzdata build-base

# Copy setup.py and install connector into /install
COPY setup.py ./
RUN pip install --prefix=/install .

# -------- Final stage: runtime --------
FROM base
WORKDIR /airbyte/integration_code

# Copy installed packages from builder
COPY --from=builder /install /usr/local

# Set timezone
COPY --from=builder /usr/share/zoneinfo/Etc/UTC /etc/localtime
RUN echo "Etc/UTC" > /etc/timezone

# Add bash for debugging (optional)
RUN apk --no-cache add bash

# Copy your connector source code
COPY main.py ./
COPY source_tripletex_put ./source_tripletex_put

# Explicitly create an airbyte user (to avoid 'no users found' in containerd)
RUN addgroup -S airbyte && adduser -S airbyte -G airbyte
USER airbyte

# Entrypoint for Airbyte
ENTRYPOINT ["python", "/airbyte/integration_code/main.py"]

# Labels required by Airbyte
LABEL io.airbyte.version=0.1.0
LABEL io.airbyte.name=airbyte/source-tripletex-put
