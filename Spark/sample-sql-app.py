import sys
from pyspark.sql import SparkSession
from pyspark import SQLContext, HiveContext
spark = SparkSession.builder.getOrCreate()
sc = spark.sparkContext
sqlContext = SQLContext(sc)
print("arguments ----", sys.argv)
df = sqlContext.sql(f'''select 'spark' as {sys.argv[1]}''')
df.show()
df.collect()




#spark-submit C:\Users\EdwinVivekN\AppData\Local\Programs\Python\Python37-32\myscripts\Spark\sample-sql-app.py helloapp