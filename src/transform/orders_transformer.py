from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    current_timestamp
)


def transform_orders(df: DataFrame) -> DataFrame:

    transformed_df = (
        df
        .dropDuplicates()
        .withColumn(
            "processed_at",
            current_timestamp()
        )
    )

    return transformed_df