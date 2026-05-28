import pandas as pd


def extract_products() -> pd.DataFrame:

    df = pd.read_csv("data/products.csv")

    return df