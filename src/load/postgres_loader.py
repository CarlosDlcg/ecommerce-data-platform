from pyspark.sql import DataFrame

from src.config.settings import (
    POSTGRES_CONFIG
)

from src.utils.logger import setup_logger

logger = setup_logger(__name__)


def write_to_postgres(
    df: DataFrame,
    table_name: str,
    schema: str = "staging"
):

    jdbc_url = (
        f"jdbc:postgresql://"
        f"{POSTGRES_CONFIG['host']}:"
        f"{POSTGRES_CONFIG['port']}/"
        f"{POSTGRES_CONFIG['database']}"
    )

    properties = {
        "user": POSTGRES_CONFIG["user"],
        "password": POSTGRES_CONFIG["password"],
        "driver": "org.postgresql.Driver"
    }

    logger.info(
        f"Writing {table_name} to PostgreSQL"
    )

    (
        df.write
        .mode("overwrite")
        .option("truncate", "true")
        .jdbc(
            url=jdbc_url,
            table=f"{schema}.{table_name}",
            properties=properties
        )
    )