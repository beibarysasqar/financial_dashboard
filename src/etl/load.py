from sqlalchemy import text
from .db_conn import get_engine

def load_to_db(df, if_exists='append'):
    engine = get_engine()
    with engine.begin() as conn:
        # Loading accounts
        accounts = df['account_name'].dropna().unique()
        for a in accounts:
            conn.execute(
                text("INSERT INTO accounts (account_name) VALUES (:a) ON CONFLICT (account_name) DO NOTHING"),
                {"a": a}
                )
        # Loading categories
        categories = df['category_name'].dropna().unique()
        for c in categories:
            conn.execute(
                text("INSERT INTO categories (name) VALUES (:c) ON CONFLICT (name) DO NOTHING"), 
                {"c": c}
                )

        account_map = {
            r['account_name']: r['account_id'] 
            for r in conn.execute(
                text("SELECT account_id, account_name FROM accounts")
                ).mappings()
                }
        category_map = {
            r['name']: r['category_id'] 
            for r in conn.execute(
                text("SELECT category_id, name FROM categories")
                ).mappings()
                }

        df['account_id'] = df['account_name'].map(account_map)
        df['category_id'] = df['category_name'].map(category_map)

        insert_df = df[['tx_date','account_id','category_id','tx_type','amount','description']]

        insert_df.to_sql(
            'transactions', 
            con=engine, 
            if_exists=if_exists, 
            index=False, 
            method='multi'
            )