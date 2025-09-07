FROM python:3.9.11-alpine3.15 as base

# -------- Build stage --------
FROM base as builder
WORKDIR /airbyte/integration_code

RUN apk --no-cache upgrade \
    && pip install --upgrade pip \
    && apk --no-cache add tzdata build-base

COPY setup.py ./
# install necessary packages to a temporary folder
RUN pip install --prefix=/install .

# -------- Final stage --------
FROM base
WORKDIR /airbyte/integration_code

COPY --from=builder /install /usr/local
COPY --from=builder /usr/share/zoneinfo/Etc/UTC /etc/localtime
RUN echo "Etc/UTC" > /etc/timezone

RUN apk --no-cache add bash

# copy payload code only
COPY source_tripletex_put ./source_tripletex_put

ENV AIRBYTE_ENTRYPOINT="python -m source_tripletex_put"
ENTRYPOINT ["python", "-m", "source_tripletex_put"]

LABEL io.airbyte.version=0.1.0
LABEL io.airbyte.name=airbyte/source-tripletex-put
