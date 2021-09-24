FROM python:3-alpine
USER root

VOLUME ["//var/run/docker.sock:/var/run/docker.sock"]

RUN addgroup python
RUN adduser --disabled-password --gecos '' python -G root -G python

WORKDIR /

RUN python -m pip install --upgrade pip
RUN pip install pylint

RUN mkdir -p /.cache/pylint

USER python