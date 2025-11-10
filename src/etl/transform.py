import pandas as pd
import numpy as np

def transform_transactions(df):
    df.columns = df.columns.str.strip().str.lower()

    df = df.rename(columns={
        'date': 'tx_date',
        'account': 'account_name',
        'category': 'category_name',
        'types': 'tx_type',
        'amount': 'amount',
        'currency': 'currency',
        'description': 'description'
    })

    df['tx_date'] = pd.to_datetime(df['tx_date']).dt.date
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce').fillna(0)

    df = df.dropna(subset=['tx_date'])
    df = df.drop_duplicates()

    return df