FROM python:3.12

RUN apt-get update && apt-get install -y postgresql-client

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .

COPY start.sh /start.sh

RUN chmod +x /start.sh

ENTRYPOINT [ "/start.sh" ]