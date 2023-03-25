Kafkaya ve straming e göre düzenlenecek

#pyspark --packages com.datastax.spark:spark-cassandra-connector_2.12:3.2.0

from pyspark.sql import SparkSession

spark = SparkSession.builder
.appName("Cassandra to Spark DataFrame")
.config("spark.cassandra.connection.host", "172.25.0.3")
.config("spark.sql.extensions", "com.datastax.spark.connector.CassandraSparkExtensions")
.getOrCreate()

df = spark.read.format("org.apache.spark.sql.cassandra")
.options(table="deneme_tablo", keyspace="cassandra_tutorial")
.load()

df.show()
