from rawIngestion.src.ingestion.service import Etl
from rawIngestion.src.deserailizer.jsonReader import *
from pyspark.sql import SparkSession
from rawIngestion.src.utils import utility
import argparse
fileDate = "fdsafs"
file_path = "C:\\data_engineering\\Fresh\\raw-data-ingestion-engine"
parser = argparse.ArgumentParser()
parser.add_argument("json_file_path",type=str)
args = parser.parse_args()
fileList = utility.get_file_list_from_path(file_path)

etl = Etl()

if __name__ == "__main__":
    print("Implementing Code...")
    schm = JsonReader.reader(args.json_file_path)
    print("The job name is: ")
    print(schm["jobName"])
    print("Unable to run the code.., it failed...")

    print("Closing all the connections...")
    if not fileList:
        print("Aborting the job as no files are identified...")
        no_file_exception = "did not find any file in the path"
        raise no_file_exception
    else:
        for file in fileList:
            print(args.json_file_path)
            etl.doETL(fileDate,file,schm)
            print("Speaking from the main class...")