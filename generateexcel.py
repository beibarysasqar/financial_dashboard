import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

n_rows = 100
start_date = datetime(2024, 1, 1)
end_date = datetime(2025, 10, 31)

accounts = ["Main Account", "Cash", "Corporate Card", "Savings"]
income_categories = ["Sales", "Consulting", "Investments", "Other Income"]
expense_categories = ["Office Supplies", "Rent", "Marketing", "Utilities", "Salaries", "Travel", "Taxes"]
currencies = ["USD"]

np.random.seed(42)
random.seed(42)

dates = [
    (start_date + timedelta(days=random.randint(0, (end_date - start_date).days))).date()
    for _ in range(n_rows)
]
accounts_col = [random.choice(accounts) for _ in range(n_rows)]

categories, amounts, types = [], [], []
for _ in range(n_rows):
    if random.random() < 0.4:  # 40% income
        cat = random.choice(income_categories)
        amt = round(random.uniform(200, 5000), 2)
        tx_type = "Income"
    else:  # 60% expense
        cat = random.choice(expense_categories)
        amt = round(-random.uniform(50, 4000), 2)
        tx_type = "Expense"
    categories.append(cat)
    amounts.append(amt)
    types.append(tx_type)

data = {
    "Date": dates,
    "Account": accounts_col,
    "Category": categories,
    "Types": types,
    "Amount": amounts,
    "Currency": [random.choice(currencies) for _ in range(n_rows)],
    "Description": [
    f"{'Income from' if amt > 0 else 'Payment for'} {cat.lower()}"
    for cat, amt in zip(categories, amounts)
]
}

df = pd.DataFrame(data).sort_values(by="Date").reset_index(drop=True)
df.to_excel("transactions.xlsx", index=False)
