FROM python:3.10-alpine

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
WORKDIR /app/src

EXPOSE 5000

CMD ["python", "app.py"]
