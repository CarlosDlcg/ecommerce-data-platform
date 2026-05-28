import pandas as pd
from sqlalchemy import create_engine

from src.config.settings import POSTGRES_CONFIG
from src.utils.logger import setup_logger

logger = setup_logger(__name__)


def extract_customers() -> pd.DataFrame:

    try:

        database_url = (
            f"postgresql://"
            f"{POSTGRES_CONFIG['user']}:"
            f"{POSTGRES_CONFIG['password']}@"
            f"{POSTGRES_CONFIG['host']}:"
            f"{POSTGRES_CONFIG['port']}/"
            f"{POSTGRES_CONFIG['database']}"
        )

        logger.info("Connecting to PostgreSQL")

        engine = create_engine(database_url)

        query = "SELECT * FROM customers"

        df = pd.read_sql(query, engine)

        logger.info(
            f"Successfully extracted {len(df)} customers"
        )

        return df

    except Exception as e:

        logger.error(
            f"PostgreSQL extraction failed: {e}"
        )

        raise