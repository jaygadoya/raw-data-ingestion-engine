from pathlib import Path
from pyspark.sql.types import StructField, StructType, StringType, IntegerType

def get_file_list_from_path(file_path: str,file_pattern: str) -> list:
    try:
        directory = Path(file_path.replace("\\","/"))
        print(f"The directory is: {directory}")
        files = []
        for items in directory.iterdir():
            if items.name.startswith(file_pattern):
                files.append(items)
        return files
    except:
        raise Exception
    finally:
        print("Reterieved all the file names.")


def fileRead(file_path: str) -> str:
    try:
        file_path = Path(file_path)
        file_content = file_path.read_text(encoding="utf-8")
        return file_content
    except:
        raise Exception
    finally:
        print("Reterived the file content...")


def jsonToSparkType(dataType: str):
    datatypeMapper = {
        "int": IntegerType(),
        "integer": IntegerType(),
        "str": StringType(),
        "string": StringType()
    }

    return datatypeMapper[dataType]