FROM python:3.10-slim

WORKDIR /app

COPY etl_pipeline.py /app/

RUN pip install pandas psycopg2-binary

CMD ["python", "etl_pipeline.py"]

