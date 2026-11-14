from pyspark.sql import SparkSession
from pyspark.sql import DataFrame


class JsonReader:
    def read(spark:SparkSession,fileOptions:dict,filePath:str) -> DataFrame :
        df = spark.read.format("json").options(**fileOptions).load(filePath)
        return df
