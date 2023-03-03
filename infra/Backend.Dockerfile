FROM python:3.11-alpine
RUN apk update
RUN apk add g++
RUN apk add make
RUN apk add sudo
RUN apk add libpq-dev postgresql-dev
RUN apk add busybox-extras
RUN addgroup --g 1024 developer
RUN adduser -u 1024 -G developer -h /home/developer -D developer
USER developer
COPY infra .
RUN pip install -r /requirements.txt
WORKDIR /usr/bin/code
