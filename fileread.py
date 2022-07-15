# from pyspark import SparkContext
# from pyspark.sql import SparkSession

# spark = (SparkSession.builder
#   .master("local")
#   .appName("chispa")
#   .getOrCreate())

# sc = SparkContext.getOrCreate()
# words = sc.parallelize ([("Finance",10),("Marketing",20),("Sales",30),("IT",40)]
# )

# df = words.toDF()
# df.show()

# file =spark.read.csv("2008-2021_US_Movies.csv")
# columns1 = ["Release_Date","Title","company","Cast ","Cast","Genre"]

# file.show()

from pyspark import SparkContext
    
logFilepath = "wordcount.txt"  
sc = SparkContext("local", "first app")
logData = sc.textFile(logFilepath).cache()
numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()
print("Lines with a: %i, lines with b: %i" % (numAs, numBs))