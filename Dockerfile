FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH=/venv/bin:$PATH

COPY . /app

RUN python -m venv /venv && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev linux-headers && \
    /venv/bin/pip install -e /app[prod] && \
    apk del .tmp-deps

WORKDIR /app/src/todo_django
