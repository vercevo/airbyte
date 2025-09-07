FROM airbyte/python-connector-base:1.1.0

# Switch to root for installation
USER root

# Ensure airbyte user exists (UID 1000 is standard)
RUN useradd -m -u 1000 -s /bin/bash airbyte

# Copy connector code
COPY . /airbyte/integration_code
WORKDIR /airbyte/integration_code

# Install connector
RUN pip install --no-cache-dir .

# Drop back to non-root user
USER airbyte

# Entrypoint for Airbyte
ENTRYPOINT ["python", "-m", "source_tripletex_put"]
