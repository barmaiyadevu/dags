from datetime import datetime, timedelta


from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from pyspark import SparkContext
from pyspark.sql import SparkSession

# spark code section
def processo_etl_spark():
    spark = (SparkSession.builder
  .master("local")
  .appName("chispa")
  .getOrCreate())

sc = SparkContext.getOrCreate()


file =spark.read.csv("2008-2021_US_Movies.csv")
columns1 = ["Release_Date","Title","company","Cast ","Cast","Genre"]

file.show()

#**************************************************************************************

#*****************DAG section************************************************************88
default_args = {
    'owner': 'jozimar',
    'start_date': datetime(2020, 11, 18),
    'retries': 10,
	  'retry_delay': timedelta(hours=1)
}
with DAG('dag_teste_spark_documento_vencido_v01',
                  default_args=default_args,
                  schedule_interval='0 1 * * *') as dag:

    task_elt_documento_pagar = PythonOperator(
        task_id='elt_documento_pagar_spark',
        python_callable=processo_etl_spark
    )

    task_elt_documento_pagar

   #*********************************************************************************     