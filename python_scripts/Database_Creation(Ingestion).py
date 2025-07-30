import pandas as pd
from sqlalchemy import create_engine
import os
import time
import logging

# Create target directories if not already present
os.makedirs(r"C:\Users\GURU PRAVEEN REDDY J\Projects\logs", exist_ok=True)
os.makedirs(r"C:\Users\GURU PRAVEEN REDDY J\Projects\db", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=r"C:\Users\GURU PRAVEEN REDDY J\Projects\logs\ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s-%(levelname)s-%(message)s",
    filemode="a"
)

# Create SQLite database connection
engine = create_engine("sqlite:///C:/Users/GURU PRAVEEN REDDY J/Projects/db/inventory_db.db")

# Function to ingest large CSV file in chunks
def ingest_large_csv(file_path, table_name, engine, chunksize=100000):
    try:
        for i, chunk in enumerate(pd.read_csv(file_path, chunksize=chunksize)):
            chunk.to_sql(table_name, con=engine, if_exists="append", index=False)
            logging.info(f"Chunk {i + 1} ingested into {table_name}")
    except Exception as e:
        logging.error(f"Error ingesting {file_path}: {str(e)}")

# Main function to load all raw data files
def load_raw_data():
    source_dir = r"C:\Users\GURU PRAVEEN REDDY J\Desktop\Datasets\Vendor Data Project Datasets\data\Cleaned Datasets"
    start_time = time.time()
    logging.info("Starting data ingestion")

    for file in os.listdir(source_dir):
        if file.endswith(".csv"):
            filepath = os.path.join(source_dir, file)
            table_name = os.path.splitext(file)[0].replace(" ", "_").lower()  # clean table name

            logging.info(f"Ingesting file: {file} into table: {table_name}")
            print(f"Ingesting: {file}")

            ingest_large_csv(filepath, table_name, engine)

    end_time = time.time()
    total_time = round((end_time - start_time) / 60, 2)
    logging.info(f"Ingestion completed in {total_time} minutes")

# Run when script is executed
if __name__ == "__main__":
    load_raw_data()
