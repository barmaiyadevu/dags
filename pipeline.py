import datetime

import pendulum

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id='pipeline 1 ',
    schedule_interval='@daily',
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    description='Hello World DAG pipline'
   
    
) as dag:

        task1=BashOperator(
            task_id="task1",
            bash_command="echo task 1"
        )

        task2=BashOperator(
            task_id="task2",
            bash_command="echo task 2"
        )
        task1.set_downstream(task2)