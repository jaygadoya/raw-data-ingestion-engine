from rawIngestion.src.ingestion.service import Etl
from pyspark.sql import SparkSession
fileList = []
fileDate = ""
if __name__ == "__main__":
    if not fileList:
        print("Aborting the job as no files are identified...")
    else:
        for file in fileList:
            Etl.etl.doETL(fileDate,file)
            print("Speaking from the main class...")