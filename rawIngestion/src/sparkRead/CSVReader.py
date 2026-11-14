from pyspark.sql import SparkSession
from pyspark.sql import DataFrame


class CsvReader:
    def read(spark:SparkSession,fileOptions:dict,filePath:str) -> DataFrame :
        df = spark.read.format("csv").options(**fileOptions).load(filePath)
        return df
