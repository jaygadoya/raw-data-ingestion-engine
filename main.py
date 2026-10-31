from rawIngestion.src.ingestion.service import Etl
from pyspark.sql import SparkSession
from rawIngestion.src.utils import utility
import argparse
fileDate = "fdsafs"
file_path = "Provide file path here..."
parser = argparse.ArgumentParser()
parser.add_argument("file_path",type=str)
args = parser.parse_args()
fileList = utility.get_file_list_from_path(file_path)

etl = Etl()

if __name__ == "__main__":
    if not fileList:
        print("Aborting the job as no files are identified...")
        no_file_exception = "did not find any file in the path"
        raise no_file_exception
    else:
        for file in fileList:
            print(args.file_path)
            etl.doETL(fileDate,file)
            print("Speaking from the main class...")