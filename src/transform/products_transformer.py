from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    col,
    current_timestamp
)

from src.utils.logger import setup_logger

logger = setup_logger(__name__)


def transform_products(df: DataFrame) -> DataFrame:

    transformed_df = (
        df
        .dropDuplicates(["product_id"])
        .filter(col("price") > 0)
        .withColumn(
            "processed_at",
            current_timestamp()
        )
    )

    input_count = df.count()
    output_count = transformed_df.count()

    logger.info(
        f"Products | Input: {input_count} | Output: {output_count}"
    )

    return transformed_df