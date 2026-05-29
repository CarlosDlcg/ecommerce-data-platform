from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="ecommerce_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["data-engineering", "portfolio"],
) as dag:

    start = BashOperator(
        task_id="start",
        bash_command="echo 'Pipeline started'"
    )

    end = BashOperator(
        task_id="end",
        bash_command="echo 'Pipeline completed'"
    )

    start >> end