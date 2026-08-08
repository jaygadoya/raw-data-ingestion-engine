from rawIngestion.src.deserailizer.jsonReader import *
from pyspark.sql import SparkSession
from pyspark.sql import *
import sys
class Etl:
    def __init__(ss:SparkSession):
        print("Inside ETL Class...")
    def doETL(ingestDate,file):
        try:
            print("Implementing Code...")
            schm = JsonReader.reader("C:\\data_engineering\\schemas.json")
            


        except:
            print("Unable to run the code.., it failed...")

        finally:
            print("Closing all the connections...")

    