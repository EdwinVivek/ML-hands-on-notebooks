import sys
from pyspark.sql import SparkSession
from pyspark import SQLContext, HiveContext
from pyspark import SparkContext, SparkConf
conf = SparkConf().set("spark.jars.packages",
"org.mongodb.spark:mongo-spark-connector:10.0.1",
    ).setAppName("mongo connector")
spark = SparkSession.builder.config(conf=conf).getOrCreate()
sc = spark.sparkContext
sqlContext = SQLContext(sc)
mongo_local = "mongodb://127.0.0.1/twt.tweets"
mongo_url = "mongodb://mani:coolcomp123@mycluster-shard-00-02.n0sqe.mongodb.net:27017/northwind.orders?authSource=admin&readPreference=secondary&ssl=true"
df  = spark.read.format("mongodb").option("spark.mongodb.connection.uri", mongo_url).load()
for i in range(10):
    df.printSchema()




#spark-submit --packages org.mongodb.spark:mongo-spark-connector:10.0.1 mongo-spark.py