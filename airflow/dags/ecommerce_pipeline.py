from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup

default_args = {
    "owner": "carlos",
    "depends_on_past": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="ecommerce_pipeline",
    description="End-to-end ecommerce data platform pipeline",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    default_args=default_args,
    max_active_runs=1,
    tags=["portfolio", "spark", "dbt", "airflow"],
) as dag:

    with TaskGroup(
        group_id="extraction"
    ) as extraction_group:

        extract_data = BashOperator(
            task_id="extract_data",
            bash_command="""
            pwd
            ls -la /opt/project/scripts
            bash /opt/project/scripts/run_extract.sh
            """
        )
    with TaskGroup(
        group_id="transformation"
    ) as transformation_group:

        transform_data = BashOperator(
            task_id="transform_data",
            bash_command="echo 'Running Spark transformations'",
            execution_timeout=timedelta(minutes=10),
        )

    with TaskGroup(
        group_id="warehouse"
    ) as warehouse_group:

        dbt_run = BashOperator(
            task_id="dbt_run",
            bash_command="echo 'Running dbt models'",
        )

        dbt_snapshot = BashOperator(
            task_id="dbt_snapshot",
            bash_command="echo 'Running dbt snapshots'",
        )

        dbt_test = BashOperator(
            task_id="dbt_test",
            bash_command="echo 'Running dbt tests'",
        )

        dbt_run >> dbt_snapshot >> dbt_test

    extraction_group >> transformation_group >> warehouse_group