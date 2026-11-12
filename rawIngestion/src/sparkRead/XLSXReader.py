from pyspark.sql import SparkSession
from pyspark.sql import DataFrame

def csvRead(spark:SparkSession,fileOptions:dict,filePath:str) -> DataFrame :
    df = spark.read.format("xlsx").options(**fileOptions).load(filePath)
    return df
