FROM  python:3.8.3-alpine

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["gunicorn","-w 4", "main:app"]

