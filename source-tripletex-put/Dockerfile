FROM airbyte/python-connector-base:1.3.0

USER root

# Ensure a valid non-root user exists
RUN useradd -m -u 1000 -s /bin/bash airbyte

COPY . /airbyte/integration_code
WORKDIR /airbyte/integration_code
RUN pip install --no-cache-dir .

# Drop to non-root
USER airbyte

ENTRYPOINT ["python", "-m", "source_tripletex_put"]
