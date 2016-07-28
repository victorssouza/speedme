FROM alpine:3.2

MAINTAINER Victor Santos

COPY src/netspeed.py /src/
COPY src/root /etc/crontabs/root
COPY requirements.txt /src/

WORKDIR /src/

RUN apk add --update python py-pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD crond -l 2 -f