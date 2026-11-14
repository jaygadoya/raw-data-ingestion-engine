from pyspark.sql import SparkSession
from pyspark.sql import DataFrame

class XlsxReader:
    def read(spark:SparkSession,fileOptions:dict,filePath:str) -> DataFrame :
        df = spark.read.format("xlsx").options(**fileOptions).load(filePath)
        return df
