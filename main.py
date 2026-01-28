from analyzer.loader import load_raw_transactions
from analyzer.cleaner import clean_transactions
from analyzer.validator import validate_transactions
from analyzer.analysis import (
    total_spend_per_user,
    monthly_spend,
    category_wise_spend,
    top_merchants,
    basic_stats,
)
from config import RAW_DATA_PATH

import os


def main():
    # 1. Load raw data
    raw_df = load_raw_transactions(RAW_DATA_PATH)

    # 2. Clean data
    clean_df = clean_transactions(raw_df)

    # validate data
    valid_df, rejected_df = validate_transactions(clean_df)

    # 4. Ensure processed directory exists
    os.makedirs("data/processed", exist_ok=True)

    # 5. Save processed data
    valid_df.to_csv("data/processed/valid_transactions.csv", index=False)
    rejected_df.to_csv("data/processed/rejected_transactions.csv", index=False)

    # 6. Save valid data to Excel
    valid_df.to_excel(
        "data/processed/valid_transactions.xlsx",
        index=False
    )

    # 7. Run analysis
    print("\n--- ANALYSIS OUTPUT ---\n")

    print("Total spend per user:")
    print(total_spend_per_user(valid_df), "\n")

    print("Monthly spend:")
    print(monthly_spend(valid_df), "\n")

    print("Category-wise spend:")
    print(category_wise_spend(valid_df), "\n")

    print("Top merchants:")
    print(top_merchants(valid_df), "\n")

    print("Basic stats:")
    print(basic_stats(valid_df))


if __name__ == "__main__":
    main()
