FROM python:3.9

COPY ./API code
WORKDIR /code
RUN pip install -r requirements.txt
