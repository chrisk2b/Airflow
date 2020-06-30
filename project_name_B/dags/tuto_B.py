"""
Code that goes along with the Airflow located at:
http://airflow.readthedocs.org/en/latest/tutorial.html
"""
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta
from lib.operators.my_first_operator import CustomDummyOperator
from project_name_B.lib.dummy_package.dummy_class import DummyClass
dummy_class = DummyClass()

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2015, 6, 1),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG("dummy_dag_project_B", default_args=default_args, schedule_interval=None)

hello_task = PythonOperator(task_id='hello_task', python_callable=dummy_class.foo, dag=dag)
dummy_task = DummyOperator(task_id='dummy_task', retries=3, dag=dag)
custom_dummy_task = CustomDummyOperator(task_id='custom_dummy_task', dag=dag)

dummy_task >> hello_task >> custom_dummy_task