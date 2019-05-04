FROM python:3.7-alpine
MAINTAINER erayozer17

# Python doesnt buffer and do everything when it comes.
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# This is for security purposes. Prevents 
# attackers to gain root access in our container.
RUN adduser -D user
USER user


# for first time use -> `docker build .`
