FROM python:3.9.0-alpine3.12
RUN apk add --no-cache --upgrade bash
RUN mkdir /ExamenU5
WORKDIR /ExamenU5
COPY . . 