import pandas as pd
from config import EXCEL_PATH
from pathlib import Path

def extract_transactions(excel_path=EXCEL_PATH, sheet_name='transactions'):
    df = pd.read_excel(excel_path, sheet_name=sheet_name, dtype=str)
    return df


# raw = Path("data/raw")
processed = Path("data/processed")
processed.mkdir(exist_ok=True, parents=True)

transactions = pd.read_excel(raw / "transactions.xlsx")
expenses = pd.read_excel(raw / "expenses.xlsx")
customers = pd.read_excel(raw / "customers.xlsx")

transactions.to_csv(processed / "transactions_clean.csv", index=False)
expenses.to_csv(processed / "expenses_clean.csv", index=False)
customers.to_csv(processed / "customers_clean.csv", index=False)

