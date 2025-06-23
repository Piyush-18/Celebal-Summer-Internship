from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from main import main

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
}

dag = DAG('mysql_data_pipeline', default_args=default_args, schedule_interval='@daily')

task = PythonOperator(task_id='run_pipeline', python_callable=main, dag=dag)
