import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from urllib.parse import quote_plus
import os


load_dotenv()


def load_file(file, table_name):

    # Read file

    if file.name.endswith(".csv"):
        df = pd.read_csv(file)

    elif file.name.endswith(".xlsx"):
        df = pd.read_excel(file)

    else:
        raise Exception("Only CSV and Excel files allowed")


    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])


    # Database connection

    password = quote_plus(
        os.getenv("DB_PASSWORD")
    )


    engine = create_engine(
        f"postgresql+psycopg2://"
        f"{os.getenv('DB_USER')}:"
        f"{password}@"
        f"{os.getenv('DB_HOST')}:"
        f"{os.getenv('DB_PORT')}/"
        f"{os.getenv('DB_NAME')}"
    )


    # Upload table

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )


    return table_name, df