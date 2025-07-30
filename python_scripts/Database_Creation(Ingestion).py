{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a2c76de4-fd3d-4574-b546-c09a4c9dbdbf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ingesting: begin_inventory.csv\n",
      "Ingesting: end_inventory.csv\n",
      "Ingesting: purchase_details.csv\n",
      "Ingesting: purchase_prices.csv\n",
      "Ingesting: sales_info.csv\n",
      "Ingesting: vendor_invoice.csv\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sqlalchemy import create_engine\n",
    "import os\n",
    "import time\n",
    "import logging\n",
    "\n",
    "# Create target directories if not already present\n",
    "os.makedirs(r\"C:\\Users\\GURU PRAVEEN REDDY J\\Projects\\logs\", exist_ok=True)\n",
    "os.makedirs(r\"C:\\Users\\GURU PRAVEEN REDDY J\\Projects\\db\", exist_ok=True)\n",
    "\n",
    "# Configure logging\n",
    "logging.basicConfig(\n",
    "    filename=r\"C:\\Users\\GURU PRAVEEN REDDY J\\Projects\\logs\\ingestion_db.log\",\n",
    "    level=logging.DEBUG,\n",
    "    format=\"%(asctime)s-%(levelname)s-%(message)s\",\n",
    "    filemode=\"a\"\n",
    ")\n",
    "\n",
    "# Create SQLite database connection\n",
    "engine = create_engine(\"sqlite:///C:/Users/GURU PRAVEEN REDDY J/Projects/db/inventory.db\")\n",
    "\n",
    "# Function to ingest large CSV file in chunks\n",
    "def ingest_large_csv(file_path, table_name, engine, chunksize=100000):\n",
    "    try:\n",
    "        for i, chunk in enumerate(pd.read_csv(file_path, chunksize=chunksize)):\n",
    "            chunk.to_sql(table_name, con=engine, if_exists=\"append\", index=False)\n",
    "            logging.info(f\"Chunk {i + 1} ingested into {table_name}\")\n",
    "    except Exception as e:\n",
    "        logging.error(f\"Error ingesting {file_path}: {str(e)}\")\n",
    "\n",
    "# Main function to load all raw data files\n",
    "def load_raw_data():\n",
    "    source_dir = r\"C:\\Users\\GURU PRAVEEN REDDY J\\Desktop\\Datasets\\Vendor Data Project Datasets\\data\"\n",
    "    start_time = time.time()\n",
    "    logging.info(\"Starting data ingestion\")\n",
    "\n",
    "    for file in os.listdir(source_dir):\n",
    "        if file.endswith(\".csv\"):\n",
    "            filepath = os.path.join(source_dir, file)\n",
    "            table_name = os.path.splitext(file)[0].replace(\" \", \"_\").lower()  # clean table name\n",
    "\n",
    "            logging.info(f\"Ingesting file: {file} into table: {table_name}\")\n",
    "            print(f\"Ingesting: {file}\")\n",
    "\n",
    "            ingest_large_csv(filepath, table_name, engine)\n",
    "\n",
    "    end_time = time.time()\n",
    "    total_time = round((end_time - start_time) / 60, 2)\n",
    "    logging.info(f\"Ingestion completed in {total_time} minutes\")\n",
    "\n",
    "# Run when script is executed\n",
    "if __name__ == \"__main__\":\n",
    "    load_raw_data()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
