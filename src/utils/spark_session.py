from pyspark.sql import SparkSession


def create_spark_session(app_name: str):

    spark = (
        SparkSession.builder
        .appName(app_name)
        .master("local[*]")
        .config(
            "spark.jars",
            "jars/postgresql-42.7.3.jar"
        )
        .config(
            "spark.sql.shuffle.partitions",
            "4"
        )
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel(
        "WARN"
    )

    return spark