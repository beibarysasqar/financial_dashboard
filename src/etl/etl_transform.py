import pandas as pd
from pathlib import Path

processed = Path("data/processed")

transactions = pd.read_csv(processed / "transactions_clean.csv", parse_dates=["date"])
expenses = pd.read_csv(processed / "expenses_clean.csv", parse_dates=["date"])

transactions["net_revenue"] = transactions["revenue"] - transactions["discount"]
transactions["month"] = transactions["date"].dt.to_period("M").dt.to_timestamp()

monthly_revenue = (
    transactions.groupby("month")["net_revenue"].sum().reset_index()
)

monthly_expenses = (
    expenses.groupby("date")["amount"].sum().reset_index()
)

monthly_revenue.to_csv(processed / "monthly_revenue.csv", index=False)
monthly_expenses.to_csv(processed / "monthly_expenses.csv", index=False)