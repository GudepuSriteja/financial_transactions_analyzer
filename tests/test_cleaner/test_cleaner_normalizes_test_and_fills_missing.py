import pandas as pd
from analyzer.cleaner import clean_transactions


def test_cleaner_normalizes_text_and_fills_missing():
    df = pd.DataFrame({
        "category": ["Food", None],
        "merchant": [None, "Amazon"],
        "payment_method": ["UPI", "CARD"],
        "status": ["SUCCESS", "failed"],
        "currency": ["INR", "USD"],
        "timestamp": ["2024-01-01 10:00:00", "invalid_date"],
        "amount": ["100", "200"]
    })

    cleaned = clean_transactions(df)
    assert cleaned.loc[0, "category"] == "food"
    assert cleaned.loc[1, "category"] == "unknown"
    assert cleaned.loc[0, "merchant"] == "unknown"
    assert pd.isna(cleaned.loc[1, "timestamp"])
    assert cleaned.loc[0, "amount"] == 100
