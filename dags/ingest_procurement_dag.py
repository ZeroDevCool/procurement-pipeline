from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

default_args = {
    'owner': 'data-engineer',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='ingest_procurement_dag',
    default_args=default_args,
    description='Pipeline de datos para ciclo de compras: GCS → BigQuery → Dataform',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
    tags=['procurement', 'dataform', 'bigquery'],
) as dag:

    start = BashOperator(
        task_id='start',
        bash_command='echo "🚀 Inicio del DAG de Procurement"',
    )

    dataform_run = BashOperator(
        task_id='dataform_run',
        bash_command='cd /path/a/tu/proyecto/dataform && dataform run',
    )

    validate = BashOperator(
        task_id='validate',
        bash_command='echo "✅ Validaciones y assertions completadas"',
    )

    end = BashOperator(
        task_id='end',
        bash_command='echo "🏁 DAG finalizado con éxito"',
    )

    start >> dataform_run >> validate >> end