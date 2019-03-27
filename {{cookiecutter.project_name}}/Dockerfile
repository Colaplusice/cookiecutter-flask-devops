FROM python:3.6
RUN adduser --disabled-login athena
WORKDIR /home/athena
COPY . .
# debian
COPY ./sources.list /etc/apt/
RUN apt-get update &&apt-get install libssl-dev
RUN pip install -r requirements.txt
RUN chmod -R +x .
ENV FLASK_ENV=production