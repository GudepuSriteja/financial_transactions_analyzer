from pathlib import Path
import pandas as pd

from config import RAW_DATA_PATH

REQUIRED_COLUMNS = {"transaction_id","user_id","timestamp",
                    "amount","currency","category","merchant","payment_method","status"}

def load_raw_transactions(path = RAW_DATA_PATH):
    """load raw tranactons data from csv,
    return:
    Pandas dataframe with raw data
    Raises:
        FilenotFoundError :if file does not exist
        ValueError :if required coulmns does not exist"""

    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"{path} does not exist")
    df = pd.read_csv(path)
    missing_columns = REQUIRED_COLUMNS - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")
    return df
