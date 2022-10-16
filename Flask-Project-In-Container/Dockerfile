FROM ubuntu:latest

MAINTAINER Aditya Mandil

RUN apt-get update -y && apt-get install -y python3-pip 

WORKDIR /app

RUN pip install flask

COPY . /app

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
