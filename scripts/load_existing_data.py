"""
Загрузка существующих очищенных данных в PostgreSQL
"""
import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

load_dotenv()

db_url = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
engine = create_engine(db_url)
logger.info("PostgreSQL connection established")

files = {
    'cpi': 'data/processed/cpi_cleaned.csv',
    'income': 'data/processed/income_cleaned.csv',
    'poverty': 'data/processed/poverty_cleaned.csv',
    'disease': 'data/processed/health_diseases_cleaned.csv',
    'medical_staff': 'data/processed/medical_staff_total.csv'
}

for table, file_path in files.items():
    if os.path.exists(file_path):
        try:
            df = pd.read_csv(file_path)
            logger.info(f"Loading {table}: {len(df)} records from {file_path}")
            df.to_sql(table, engine, if_exists='replace', index=False)
            logger.info(f"Loaded {len(df)} records into {table}")
        except Exception as e:
            logger.error(f"Error loading {table}: {e}")
    else:
        logger.warning(f"File not found: {file_path}")

with engine.connect() as conn:
    for table in files.keys():
        result = conn.execute(text(f"SELECT COUNT(*) FROM {table}"))
        count = result.fetchone()[0]
        logger.info(f"{table}: {count} records in database")

logger.info("Load completed")
