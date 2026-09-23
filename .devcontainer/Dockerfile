FROM apache/airflow:3.3.0

COPY requirements/ /tmp/requirements/

RUN pip install --no-cache-dir \
    -r /tmp/requirements/airflow.txt \
    -r /tmp/requirements/dev.txt \
    -r /tmp/requirements/mlflow.txt