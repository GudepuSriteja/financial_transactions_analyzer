import pandas as pd


def total_spend_per_user(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("user_id")["amount"]
        .sum()
        .reset_index(name="total_spend")
    )


def monthly_spend(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["month"] = df["timestamp"].dt.to_period("M")

    return (
        df.groupby("month")["amount"]
        .sum()
        .reset_index()
    )


def category_wise_spend(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("category")["amount"]
        .sum()
        .reset_index(name="total_spend")
        .sort_values("total_spend", ascending=False)
    )


def top_merchants(df: pd.DataFrame, top_n: int = 5) -> pd.DataFrame:
    return (
        df.groupby("merchant")["amount"]
        .sum()
        .reset_index(name="total_spend")
        .sort_values("total_spend", ascending=False)
        .head(top_n)
    )


def basic_stats(df: pd.DataFrame) -> dict:
    return {
        "total_transactions": len(df),
        "total_amount": df["amount"].sum(),
        "average_amount": df["amount"].mean(),
        "max_transaction": df["amount"].max(),
    }
