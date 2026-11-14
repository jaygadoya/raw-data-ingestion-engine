from pyspark.sql import SparkSession
from pyspark.sql import *
import sys
from pyspark.sql.types import StructType, StructField
from ..utils import utility
from rawIngestion.src.sparkRead import CSVReader, JSONReader, XLSXReader
class Etl:
    def __init__(ss:SparkSession):
        print("Inside ETL Class...")
    def doETL(self,ingestDate: str,file: str,schm: dict) -> None:
        try:
            print("Implementing Code...")
            fieldList = []
            for jsSchm in schm["fileField"]:
                fieldList.append(StructField(jsSchm["name"],utility.jsonToSparkType(jsSchm["dataType"]),jsSchm["nullable"]))
            fileSchema = StructType(fieldList)
            print(f"The fileschema is: {fileSchema}")
            # Creating an instance based on the file type.
            fileTypeMapper = {"csv":CSVReader.CsvReader(),
                              "json": JSONReader.JsonReader(),
                              "xlsx":XLSXReader.XlsxReader()}
            df = fileTypeMapper[schm["fileType"]].read(schm["fileOptions"],schm["filePath"])
            

                      
        except:
            raise Exception
        finally:
            print("Closing all the connections...")