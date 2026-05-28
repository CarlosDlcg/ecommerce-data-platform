from src.utils.spark_session import (
    create_spark_session
)

spark = create_spark_session(
    "inspect-staging"
)

customers_df = spark.read.parquet(
    "data/staging/customers"
)

print("\nCUSTOMERS")
customers_df.printSchema()
customers_df.show()

products_df = spark.read.parquet(
    "data/staging/products"
)

print("\nPRODUCTS")
products_df.printSchema()
products_df.show()

orders_df = spark.read.parquet(
    "data/staging/orders"
)

print("\nORDERS")
orders_df.printSchema()
orders_df.show()

spark.stop()