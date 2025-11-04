from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CONN_STR = f"postgresql+psycopg2://postgres:12345@localhost:5432/finance_dashboard"
engine = create_engine(CONN_STR, echo=False)
SessionLocal = sessionmaker(bind=engine)