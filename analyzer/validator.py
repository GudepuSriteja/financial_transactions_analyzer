import pandas as pd
from datetime import datetime
from config import SUPPORTED_CURRENCY, VALID_STATUS


def validate_transactions(df: pd.DataFrame):
    """
    Validate cleaned transaction data.

    Returns:
        valid_df     -> rows that pass all rules
        rejected_df  -> rows that fail any rule
    """

    valid_rows = []
    rejected_rows = []
    # Used to detect future transactions
    # current_time = pd.Timestamp(datetime.utcnow())
    current_time = pd.Timestamp(datetime.utcnow())

    for _, row in df.iterrows():
        reasons = []

        # 1. Timestamp must exist
        if pd.isna(row["timestamp"]):
            reasons.append("invalid_timestamp")

        # 2. Timestamp should not be in the future
        elif row["timestamp"] > current_time:
            reasons.append("future_timestamp")

        # 3. Amount must exist and not be zero
        if pd.isna(row["amount"]) or row["amount"] == 0:
            reasons.append("invalid_amount")

        # 4. Currency must be supported
        if row["currency"] not in SUPPORTED_CURRENCY:
            reasons.append("invalid_currency")

        # 5. Status must be valid
        if row["status"] not in VALID_STATUS:
            reasons.append("invalid_status")

        # Decide whether row is valid or rejected
        if reasons:
            row_copy = row.copy()
            row_copy["rejection_reason"] = ",".join(reasons)
            rejected_rows.append(row_copy)
        else:
            valid_rows.append(row)

    # convert lists back to dataframes
    valid_df = pd.DataFrame(valid_rows)
    rejected_df = pd.DataFrame(rejected_rows)

    # Remove duplicate transaction IDs from valid data
    if not valid_df.empty:
        valid_df = valid_df.drop_duplicates(subset=["transaction_id"])

    return valid_df, rejected_df
