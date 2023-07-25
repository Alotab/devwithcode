FROM python:3.11.4-alpine3.18
LABEL maintainer="devwithcode.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./app /app

WORKDIR /app 
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt && \
    adduser --disable-password --no-create-home app

ENV PATH="/py/bin:$PATH"

USER app