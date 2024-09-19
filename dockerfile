FROM python:3.11.4-slim-buster

RUN apt update -y && \
    apt install -y azurecli && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app


RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]
