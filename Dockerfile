FROM python:3.13-bookworm AS builder

WORKDIR /app

RUN pip install poetry==1.8.4

COPY poetry.lock pyproject.toml ./

RUN POETRY_VIRTUALENVS_IN_PROJECT=true poetry install --without=test

FROM python:3.13-slim-bookworm AS runtime

WORKDIR /app

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY tibber_technical_case ./tibber_technical_case

ENTRYPOINT ["gunicorn", "--workers=4", "-b 0.0.0.0:5000", "tibber_technical_case.app:app"]
