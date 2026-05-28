from pathlib import Path
from pyspark.sql import DataFrame

from src.utils.logger import setup_logger

logger = setup_logger(__name__)


def save_staging_data(
    df: DataFrame,
    domain: str
) -> None:

    output_path = Path(
        f"data/staging/{domain}"
    )

    logger.info(
        f"Writing staging data -> {output_path}"
    )

    (
        df.write
        .mode("overwrite")
        .parquet(str(output_path))
    )