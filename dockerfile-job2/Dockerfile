FROM python:3.8.12-slim-buster
WORKDIR /app
COPY . .
RUN pip install psycopg-binary


CMD ["python3", "job2-postgrse-write.py"]