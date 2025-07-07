FROM apache/airflow:2.8.0

USER root

# (wait-for-it.sh is no longer needed, so these lines are removed)
# COPY wait-for-it.sh /wait-for-it.sh
# RUN chmod +x /wait-for-it.sh

USER airflow

RUN pip install --upgrade pip && \
    pip install dbt-postgres==1.7.4 pyspark==3.5.0 pandas sqlalchemy psycopg2-binary
