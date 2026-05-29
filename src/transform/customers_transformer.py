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

    input_count = df.count()
    output_count = transformed_df.count()

    logger.info(
        f"Customers | Input: {input_count} | Output: {output_count}"
    )

    return transformed_df