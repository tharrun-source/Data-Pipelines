FROM apache/airflow:2.9.2
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" xmltodict