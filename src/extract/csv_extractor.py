import pandas as pd

from src.utils.logger import setup_logger

logger = setup_logger(__name__)

def extract_products() -> pd.DataFrame:

    try:

        logger.info(
                f"Fetching products from CSV file"
            )

        df = pd.read_csv("data/products.csv")

        logger.info(
            f"Successfully extracted {len(df)} products"
        )

    except Exception as e:

        logger.error(
            f"Failed to extract products: {e}"
        )

        raise

    return df