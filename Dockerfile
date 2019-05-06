FROM python:3.7-alpine
MAINTAINER erayozer17

# Python doesnt buffer and do everything when it comes.
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# This is for security purposes. Prevents 
# attackers to gain root access in our container.
RUN adduser -D user
USER user


# for first time use -> `docker build .`
