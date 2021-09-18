FROM python:3.8.5-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade -y

RUN pip install --upgrade pip

COPY ./req.txt .
RUN pip install -r reqmin.txt

COPY . .

