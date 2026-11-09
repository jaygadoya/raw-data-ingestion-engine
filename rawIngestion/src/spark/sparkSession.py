from pyspark.sql import SparkSession

def getSparkSession(app_name: str) -> SparkSession:
    spark = SparkSession.builder.appName(app_name).enableHiveSupport().getOrCreate()
    return spark

ss = getSparkSession("Hello")

df = ss.createDataFrame([{"Name":"Alice in the Wonderland","Age":"28"}])
df.show()