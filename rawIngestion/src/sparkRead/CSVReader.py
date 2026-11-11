from pyspark.sql import SparkSession

def csvRead(spark:SparkSession,fileOptions:dict,filePath:str):
    df = spark.read.format("csv").options(**fileOptions).load(filePath)