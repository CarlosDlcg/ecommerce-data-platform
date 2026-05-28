from pathlib import Path

from src.utils.spark_session import (
    create_spark_session
)

from src.transform.schemas import (
    CUSTOMERS_SCHEMA,
    PRODUCTS_SCHEMA
)

from src.transform.customers_transformer import (
    transform_customers
)

from src.transform.products_transformer import (
    transform_products
)

from src.transform.orders_transformer import (
    transform_orders
)

from src.load.staging_loader import (
    save_staging_data
)

from src.utils.logger import setup_logger

logger = setup_logger(__name__)


def get_latest_file(path: str):

    files = list(Path(path).glob("*.csv"))

    latest_file = max(
        files,
        key=lambda x: x.stat().st_mtime
    )

    return str(latest_file)


def main():

    spark = create_spark_session(
        "ecommerce-staging-pipeline"
    )

    logger.info("Starting Spark transformations")

    # CUSTOMERS

    customers_file = get_latest_file(
        "data/raw/customers"
    )

    customers_df = spark.read.csv(
        customers_file,
        header=True,
        schema=CUSTOMERS_SCHEMA
    )

    customers_df = transform_customers(
        customers_df
    )

    save_staging_data(
        customers_df,
        "customers"
    )

    # PRODUCTS

    products_file = get_latest_file(
        "data/raw/products"
    )

    products_df = spark.read.csv(
        products_file,
        header=True,
        schema=PRODUCTS_SCHEMA
    )

    products_df = transform_products(
        products_df
    )

    save_staging_data(
        products_df,
        "products"
    )

    # ORDERS

    orders_file = get_latest_file(
        "data/raw/orders"
    )

    orders_df = spark.read.csv(
        orders_file,
        header=True,
        inferSchema=True
    )

    orders_df = transform_orders(
        orders_df
    )

    save_staging_data(
        orders_df,
        "orders"
    )

    logger.info(
        "Spark transformations completed"
    )

    spark.stop()


if __name__ == "__main__":
    main()