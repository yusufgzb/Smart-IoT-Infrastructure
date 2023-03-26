from pyspark.sql.functions import from_json
from pyspark.sql.types import StructType, StructField, DoubleType, TimestampType, IntegerType, StringType,FloatType

spark = SparkSession.builder \
    .appName("Cassandra to Spark DataFrame") \
    .config("spark.cassandra.connection.host", "cassandra-docker") \
    .config("spark.sql.extensions", "com.datastax.spark.connector.CassandraSparkExtensions") \
    .getOrCreate()

# Cassandra tablosunun ismi
table_name = "energy_data"

# Cassandra anahtar uzayının ismi
keyspace = "cassandra_tutorial"

# StructType oluşturma
energy_data_schema = StructType([
        StructField("time", TimestampType(), True),
        StructField("apparenttemperature", FloatType(), True),
        StructField("barn_kw", DoubleType(), True),
        StructField("cloudcover", StringType(), True),
        StructField("dewpoint", DoubleType(), True),
        StructField("dishwasher_kw", DoubleType(), True),
        StructField("fridge_kw", DoubleType(), True),
        StructField("furnace_1_kw", DoubleType(), True),
        StructField("furnace_2_kw", DoubleType(), True),
        StructField("garage_door_kw", DoubleType(), True),
        StructField("gen_kw", DoubleType(), True),
        StructField("home_office_kw", DoubleType(), True),
        StructField("house_overall_kw", DoubleType(), True),
        StructField("humidity", DoubleType(), True),
        StructField("icon", StringType(), True),
        StructField("kitchen_12_kw", DoubleType(), True),
        StructField("kitchen_14_kw", DoubleType(), True),
        StructField("kitchen_38_kw", DoubleType(), True),
        StructField("living_room_kw", DoubleType(), True),
        StructField("microwave_kw", DoubleType(), True),
        StructField("precipintensity", DoubleType(), True),
        StructField("precipprobability", IntegerType(), True),
        StructField("pressure", DoubleType(), True),
        StructField("solar_kw", DoubleType(), True),
        StructField("summary", StringType(), True),
        StructField("temperature", DoubleType(), True),
        StructField("use_kw", DoubleType(), True),
        StructField("visibility", DoubleType(), True),
        StructField("well_kw", DoubleType(), True),
        StructField("windbearing", IntegerType(), True),
        StructField("windspeed", DoubleType(), True),
        StructField("wine_cellar_kw", DoubleType(), True)
])
# Kafka verilerini okuma ve DataFrame oluşturma
df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "kafka-docker:29092") \
  .option("subscribe", "ornek") \
  .load()

# JSON verileri StructType'a dönüştürme
df = df.select(from_json(df["value"].cast("string"), energy_data_schema).alias("activation")) 

df = df.select("activation.time","activation.apparenttemperature", "activation.barn_kw", "activation.cloudcover", "activation.dewpoint",
                "activation.dishwasher_kw", "activation.fridge_kw", "activation.furnace_1_kw", "activation.furnace_2_kw",
                "activation.garage_door_kw", "activation.gen_kw", "activation.home_office_kw", "activation.humidity",
                "activation.house_overall_kw", "activation.icon", "activation.kitchen_12_kw", "activation.kitchen_14_kw",
                "activation.kitchen_38_kw", "activation.living_room_kw", "activation.microwave_kw", "activation.precipintensity",
                "activation.precipprobability", "activation.pressure", "activation.solar_kw", "activation.summary",
                "activation.temperature", "activation.visibility", "activation.well_kw",
                "activation.windbearing", "activation.windspeed", "activation.wine_cellar_kw")# Cassandra tablosuna yazma


df.writeStream \
    .format("org.apache.spark.sql.cassandra") \
    .option("checkpointLocation", "/tmp/checkpoint") \
    .option("keyspace", keyspace) \
    .option("table", table_name) \
    .start()
