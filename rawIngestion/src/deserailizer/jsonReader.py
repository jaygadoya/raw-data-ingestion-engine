import json
from pyspark.sql.types import StructField, StructType, StringType, IntegerType, MapType, DateType
class JsonReader:
    def __init__():
        print("Getting the Json Reader")

    def reader(filePath):
        print("Reading in progress...")
        with open(filePath) as f:
            dictSchema = json.load(f)
        print("Json deserialization successful..")

        return dictSchema

    def jsonToSparkType(jsonType):
        try:
            dType = {
                "string" : StringType(),
                "str" : StringType(),
                "integer" : IntegerType(),
                "int" : IntegerType(),
                "date" : DateType(),
                "map" : MapType()
            }
            return dType[jsonType]
        except:
            print("The given data type is invalid, please check for it...")

        finally:
            print("Completed the mapping..")


    