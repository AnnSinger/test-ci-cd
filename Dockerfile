FROM python:3.9

COPY . /app
COPY requirements.txt .

RUN apt-get update && apt-get install -y
RUN pip install -r ./requirements.txt

WORKDIR /app

ENTRYPOINT ["pytest"]