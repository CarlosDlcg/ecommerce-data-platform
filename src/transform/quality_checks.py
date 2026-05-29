from pyspark.sql import DataFrame


def validate_not_empty(
    df: DataFrame,
    dataset_name: str
) -> None:

    if df.count() == 0:
        raise ValueError(
            f"{dataset_name} is empty"
        )