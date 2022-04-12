FROM python:3.10-alpine

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev curl

WORKDIR /opt

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
