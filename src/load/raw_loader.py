from pathlib import Path
import pandas as pd

from src.utils.logger import setup_logger

logger = setup_logger(__name__)


def save_raw_data(
    df: pd.DataFrame,
    domain: str,
    file_name: str
) -> None:

    try:

        output_path = Path(f"data/raw/{domain}")

        output_path.mkdir(
            parents=True,
            exist_ok=True
        )

        full_path = output_path / f"{file_name}.csv"

        df.to_csv(
            full_path,
            index=False
        )

        logger.info(
            f"Saved RAW data -> {full_path}"
        )

    except Exception as e:

        logger.error(
            f"Failed saving RAW data: {e}"
        )

        raise