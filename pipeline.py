from datetime import datetime, timedelta
from airflow import DAG
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator


#*****************DAG section************************************************************88
default_args = {
    'owner': 'jozimar',
    'start_date': datetime(2020, 11, 18),
    'retries': 10,
	  'retry_delay': timedelta(hours=1)
}
dag_spark =DAG('dag_teste_spark_documento_vencido_v01',
                  default_args=default_args,
                  schedule_interval='0 12 * * *') 

spark_submit_local = SparkSubmitOperator(
		application ='fileread.py' ,
		conn_id= 'spark_local', 
		task_id='spark_submit_task', 
		dag=dag_spark
		)

spark_submit_local

if __name__ == "__main__":
    dag_spark.cli()

   #*********************************************************************************     