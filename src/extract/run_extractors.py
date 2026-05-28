from datetime import datetime

from src.extract.postgres_extractor import extract_customers
from src.extract.csv_extractor import extract_products
from src.extract.api_extractor import extract_orders

from src.load.raw_loader import save_raw_data


def main():

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    customers_df = extract_customers()
    save_raw_data(
        customers_df,
        "customers",
        f"customers_{timestamp}"
    )

    products_df = extract_products()
    save_raw_data(
        products_df,
        "products",
        f"products_{timestamp}"
    )

    orders_df = extract_orders()
    save_raw_data(
        orders_df,
        "orders",
        f"orders_{timestamp}"
    )

    print("All extractions completed successfully!")


if __name__ == "__main__":
    main()