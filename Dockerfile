FROM python:3.8

RUN apt-get update
RUN apt-get install -y git python3-pip

WORKDIR /etc
RUN mkdir repeatbot
WORKDIR /etc/repeatbot

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "/etc/repeatbot/main.py"]

