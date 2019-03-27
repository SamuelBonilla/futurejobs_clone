FROM python:3

RUN apt-get update
RUN apt-get install libpq-dev

WORKDIR /usr/src/app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

EXPOSE 1337

WORKDIR /usr/src/app/landing

CMD ["python", "app.py"]

