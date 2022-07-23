FROM python:3.8.13-bullseye

WORKDIR /app

COPY . /app/

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]
