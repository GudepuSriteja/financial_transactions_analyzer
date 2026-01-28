import pandas as pd
from analyzer.cleaner import clean_transactions



def test_cleaner_handles_spaces_and_empty_strings():
    df = pd.DataFrame({
        "category": ["  FOOD  ", ""],
        "merchant": ["amazon", ""],
        "payment_method": ["UPI", "CARD"],
        "status": [" SUCCESS ", "FAILED"],
        "currency": ["INR", "USD"],
        "timestamp": ["2024-01-01 10:00:00", "2024-01-02 11:00:00"],
        "amount": ["500", "600"]
    })

    cleaned = clean_transactions(df)

    assert cleaned.loc[0, "category"] == "food"
    assert cleaned.loc[1, "category"] == "unknown"
    assert cleaned.loc[0, "merchant"] == "amazon"
    assert cleaned.loc[1, "merchant"] == "unknown"
