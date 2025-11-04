import pandas as pd
from sqlalchemy import text
from db import engine, SessionLocal

def load_transactions(csv_path):