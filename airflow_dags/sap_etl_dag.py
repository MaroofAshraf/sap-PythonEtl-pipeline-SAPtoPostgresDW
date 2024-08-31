from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from src.extract.sap_extract import extract_data
from src.transform.transform_data import transform_data
from src.load.load_to_postgres import load_to_postgres

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

dag = DAG('sap_etl_dag', default_args=default_args, schedule_interval='@daily')

def etl_task():
    df = extract_data('MATERIALS')
    df_transformed = transform_data(df)
    load_to_postgres(df_transformed, 'materials')

etl_operator = PythonOperator(
    task_id='etl_task',
    python_callable=etl_task,
    dag=dag,
)

etl_operator
