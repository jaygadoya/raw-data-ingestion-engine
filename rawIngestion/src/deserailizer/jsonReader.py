import json
from pyspark.sql.types import StructField, StructType, StringType, IntegerType, MapType, DateType

# This class is to read the JSON Config file from the Path.
class JsonReader:
    '''The class contains reader function to perform deserializer operation on the config file.
       The config file will contain all the metadata related information for the tables and files.
       return '''
    
    def __init__():
        print("Getting the Json Reader")

    def reader(filePath) -> dict:
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


    