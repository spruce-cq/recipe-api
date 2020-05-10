FROM python:3.7-alpine

MAINTAINER ChangQing

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r ./requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY ./app /app

RUN adduser -D django
USER django