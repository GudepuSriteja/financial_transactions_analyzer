import pandas as pd
from analyzer.analysis import (
    total_spend_per_user
)


def sample_df():
    return pd.DataFrame({
        "user_id": ["u1", "u1", "u2", "u2"],
        "amount": [100, 200, 300, 400],
        "category": ["food", "travel", "food", "shopping"],
        "merchant": ["A", "B", "A", "C"],
        "timestamp": pd.to_datetime([
            "2024-01-10",
            "2024-01-15",
            "2024-02-01",
            "2024-02-05",
        ])
    })


def test_total_spend_per_user():
    df = sample_df()

    result = total_spend_per_user(df)

    assert len(result) == 2
    assert result.loc[result["user_id"] == "u1", "total_spend"].iloc[0] == 300
    assert result.loc[result["user_id"] == "u2", "total_spend"].iloc[0] == 700
