FROM python:3.9.11-alpine3.15 as base

# -------- Build stage --------
FROM base as builder
WORKDIR /airbyte/integration_code

RUN apk --no-cache upgrade \
    && pip install --upgrade pip \
    && apk --no-cache add tzdata build-base

# copy full source (setup.py + package folder)
COPY . .

# install into temp prefix
RUN pip install --prefix=/install .

# -------- Final stage --------
FROM base
WORKDIR /airbyte/integration_code

# bring installed packages + timezone
COPY --from=builder /install /usr/local
COPY --from=builder /usr/share/zoneinfo/Etc/UTC /etc/localtime
RUN echo "Etc/UTC" > /etc/timezone

RUN apk --no-cache add bash

# copy all source (so spec.json etc. is available inside container)
COPY . .

# install package properly into final image
RUN pip install .

# run as non-root user
USER 1000

# Airbyte expects this
ENV AIRBYTE_ENTRYPOINT="python -m source_tripletex_put"
ENTRYPOINT ["python", "-m", "source_tripletex_put"]

LABEL io.airbyte.version=0.1.0
LABEL io.airbyte.name=airbyte/source-tripletex-put
