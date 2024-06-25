FROM apache/airflow:2.9.2
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" xmltodictcd
#this above command is crucial never forget the syntax i got it from https://airflow.apache.org/docs/docker-stack/build.html
