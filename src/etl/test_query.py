import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:12345@localhost:5432/finance_dashboard")

with open("sql/queries.sql", "r") as f:
    query = f.read()

df = pd.read_sql(query, engine)
print(df)

