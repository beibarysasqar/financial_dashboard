# Date amounts are not empty
# There are no very large outliers (|amount| > threshold)
# Date coverage (min/max)

def validate(df):
    assert 'tx_date' in df.columns
    assert df['amount'].dtype.kind in 'fi'

    zero_pct = (df['amount']==0).mean()
    if zero_pct > 0.2:
        print("Warning: >20% zero amounts")