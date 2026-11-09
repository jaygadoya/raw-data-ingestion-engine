from pyspark.sql import SparkSession

def getSparkSession(app_name: str) -> SparkSession:
    spark = SparkSession.Builder.appName(app_name).getOrCreate()
    return spark