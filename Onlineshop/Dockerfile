FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . /usr/src/app/