import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from urllib.parse import quote_plus
import os

load_dotenv()

# Load CSV
df = pd.read_csv("data/Loan_default.csv")

print("Rows:", len(df))
print(df.head())


# Encode password
password = quote_plus(os.getenv("DB_PASSWORD"))


# PostgreSQL connection
engine = create_engine(
    f"postgresql://"
    f"{os.getenv('DB_USER')}:{password}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)


# Load data
df.to_sql(
    "loan_default",
    engine,
    if_exists="replace",
    index=False
)


print("✅ Loan dataset loaded into PostgreSQL")