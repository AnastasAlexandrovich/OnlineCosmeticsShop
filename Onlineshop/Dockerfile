FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN apk add --no-cache libressl-dev musl-dev libffi-dev
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . /usr/src/app/