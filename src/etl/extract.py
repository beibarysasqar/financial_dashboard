import pandas as pd
from pathlib import Path

RAW_DIR = Path(__file__).resolve().parents[2] / "data" / "processed"

def extract_from_csv(filename: str) -> pd.DataFrame:
    path = RAW_DIR / filename
    df = pd.read_csv(path)
    return df
