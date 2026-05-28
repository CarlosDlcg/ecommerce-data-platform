from dotenv import load_dotenv
import os

load_dotenv()

POSTGRES_CONFIG = {
    "user": os.getenv("POSTGRES_USER"),
    "password": os.getenv("POSTGRES_PASSWORD"),
    "host": os.getenv("POSTGRES_HOST"),
    "port": os.getenv("POSTGRES_PORT"),
    "database": os.getenv("POSTGRES_DB"),
}

API_URL = os.getenv(
    "API_URL",
    "https://fakestoreapi.com/carts"
)

RAW_DATA_PATH = "data/raw"

API_TIMEOUT = 10
API_RETRIES = 3