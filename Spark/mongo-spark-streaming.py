import sys
from pyspark.sql import SparkSession
from pyspark import SQLContext, HiveContext
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
conf = SparkConf().set("spark.jars.packages",
"org.mongodb.spark:mongo-spark-connector:10.0.1",
    ).setMaster("local[*]").setAppName("mongo streaming connector")
spark = SparkSession.builder.config(conf=conf).getOrCreate()
sc = spark.sparkContext
sqlContext = SQLContext(sc)
streamingContext = StreamingContext(sc, 2)
mongo_local = "mongodb://127.0.0.1/twt.tweets"
mongo_url = "mongodb://mani:coolcomp123@mycluster-shard-00-02.n0sqe.mongodb.net:27017/mydb.MyCol?authSource=admin&readPreference=secondary&ssl=true"

query=(spark.readStream.format("mongodb")
.option('spark.mongodb.connection.uri', mongo_url)
    	.option('spark.mongodb.database', 'mydb') \
    	.option('spark.mongodb.collection', 'MyCol') \
.option('spark.mongodb.change.stream.publish.full.document.only','true') \
    	.option("forceDeleteTempCheckpointLocation", "true") \
    	.load())

query.printSchema()
print("\nIs Streaming: ", query.isStreaming)


query2=(query.writeStream \
  .outputMode("append") \
  .option("forceDeleteTempCheckpointLocation", "true") \
  .format("console") \
  .trigger(continuous="1 second")
  .start());

#spark-submit --packages org.mongodb.spark:mongo-spark-connector:10.0.1 mongo-spark-streaming.py