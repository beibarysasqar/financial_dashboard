from .extract import extract_from_csv
from .transform import transform_transactions
from .load import load_to_db
def main():
    df_raw = extract_from_csv("transactions.csv")
    df_clean = transform_transactions(df_raw)
    load_to_db(df_clean)

if __name__ == "__main__":
    main()