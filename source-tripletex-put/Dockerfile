FROM airbyte/python-connector-base:1.1.0

# Switch to root to install deps
USER root

# Install your connector
COPY . /airbyte/integration_code
WORKDIR /airbyte/integration_code
RUN pip install .

# Drop back to airbyte user
USER airbyte

# Entrypoint for Airbyte to run
ENTRYPOINT ["python", "-m", "source_tripletex_put"]
