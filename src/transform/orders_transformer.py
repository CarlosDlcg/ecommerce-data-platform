from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    current_timestamp
)


def transform_orders(df: DataFrame) -> DataFrame:

    technical_columns = [
        "__v"
    ]

    existing_columns = [
        c for c in technical_columns
        if c in df.columns
    ]

    transformed_df = (
        df
        .drop(*existing_columns)
        .dropDuplicates()
        .withColumn(
            "processed_at",
            current_timestamp()
        )
    )

    return transformed_df