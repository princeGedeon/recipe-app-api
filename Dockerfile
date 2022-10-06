FROM python:3.9.14-alpine3.16

LABEL maintainer="recipeapi.com"

ENV PYTHONBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt

COPY ./requirementsdev.txt /tmp/requirementsdev.txt

COPY ./app /app

ARG DEV=false

WORKDIR /app

EXPOSE 8000

RUN python -m venv /py && \
/py/bin/pip install --upgrade pip && \
if [ $DEV = "true" ]; \
then /py/bin/pip install -r /tmp/requirementsdev.txt; \
fi && \
/py/bin/pip install -r /tmp/requirements.txt && \
rm -rf /tmp && \
adduser \
--disabled-password \
--no-create-home \
django-user

ENV PATH="/py/bin:$PATH"

USER django-user
