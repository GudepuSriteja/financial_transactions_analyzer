
import pandas as pd


def clean_transactions(df):
    """
    Perform soft cleaning and normalization on raw transaction data.
    No rows are dropped here.

    Steps:
    1. Normalize text columns (strip, lowercase)
    2. Replace empty/nan-like values with None
    3. Fill soft-missing fields (category, merchant)
    4. Parse timestamps safely
    5. Convert amount to numeric
    """

    df = df.copy()

    # defining the columns to normalize

    text_columns = ["category", "merchant","payment_method", "status","currency"]
    for col in text_columns:
        df[col] = (
            df[col]
            .astype(str)
            .str.strip()
            .str.lower()
            .replace({"nan": None, "none": None, "": None})
        )

    # Fill soft missing fields
    df["category"] = df["category"].fillna("unknown")
    df["merchant"] = df["merchant"].fillna("unknown")

    # errors="coerce, converts anything invalid to NaT.
    # 2024-14-01 15:00:00 (invalid month) → NaT
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce", utc=True)

    # Convert amount column
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    return df
