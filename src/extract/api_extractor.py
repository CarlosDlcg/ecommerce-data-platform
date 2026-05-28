import time
import requests
import pandas as pd

from src.config.settings import (
    API_URL,
    API_TIMEOUT,
    API_RETRIES
)

from src.utils.logger import setup_logger

logger = setup_logger(__name__)


def extract_orders() -> pd.DataFrame:

    for attempt in range(API_RETRIES):

        try:

            logger.info(
                f"Fetching orders from API | Attempt {attempt + 1}"
            )

            response = requests.get(
                API_URL,
                timeout=API_TIMEOUT
            )

            response.raise_for_status()

            data = response.json()

            df = pd.json_normalize(data)

            logger.info(
                f"Successfully extracted {len(df)} orders"
            )

            return df

        except requests.exceptions.RequestException as e:

            logger.error(
                f"API extraction failed: {e}"
            )

            time.sleep(2)

    raise Exception(
        "API extraction failed after retries"
    )