FROM python:3.7.9

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

COPY . .

RUN pip install --upgrade pip setuptools && pip install -r requirements.txt