FROM python:3.13-bookworm AS builder

WORKDIR /app

RUN pip install poetry==1.8.4

COPY . .

RUN poetry install

#FROM python:3.13-slim-bookworm AS runtime
#
#ENV VIRTUAL_ENV=/app/.venv \
#    PATH="/app/.venv/bin:$PATH"
#
#COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

#ENTRYPOINT ["python", "-m", "tibber_technical_case.app"]
