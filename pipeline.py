from datetime import datetime, timedelta
from airflow import DAG
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator


#*****************DAG section************************************************************88
default_args = {
    'owner': 'devesh barmaiya',
    'retries': 1,
	  'retry_delay': timedelta(hours=1)
}
dag_spark =DAG('sparksubmit_v03',
                  default_args=default_args,
                  schedule_interval='* * * * *') 

# IMPORTATNT spark_local connection define in airflow connection  to run local

# connection id : spark_local
# host : local[*]
# exra : {"queue","default", "master":"local[*]", "spark-home":"/opt/spark/spark-3.1-bin-hadoop2.7",
# "spark-binary":"spark-submit", "namespace":"default"
# }
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