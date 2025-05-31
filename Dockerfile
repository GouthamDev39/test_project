FROM python:3.10-slim

WORKDIR /home/app

RUN apt-get update \
    && apt-get install -y --no-install-recommends postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x start_up.sh

EXPOSE 8000

CMD ["./start_up.sh"]
