from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    col,
    current_timestamp
)


def transform_customers(df: DataFrame) -> DataFrame:

    transformed_df = (
        df
        .dropDuplicates(["customer_id"])
        .filter(col("email").isNotNull())
        .withColumn(
            "processed_at",
            current_timestamp()
        )
    )

    return transformed_df