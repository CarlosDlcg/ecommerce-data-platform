from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    col,
    current_timestamp
)


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

    return transformed_df