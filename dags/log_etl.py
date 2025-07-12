from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1
}

with DAG(
    dag_id='netflix_watch_logs_etl',
    default_args=default_args,
    schedule_interval=None,  # Manual trigger only
    catchup=False,
    tags=['netflix', 'watch_logs', 'etl'],
    description='ETL pipeline for Netflix watch logs data using pandas and PostgreSQL'
) as dag:

    run_netflix_etl = BashOperator(
        task_id='run_netflix_load_script',
        bash_command='python /opt/airflow/etl/netflix_load.py'
    )

    run_netflix_etl
