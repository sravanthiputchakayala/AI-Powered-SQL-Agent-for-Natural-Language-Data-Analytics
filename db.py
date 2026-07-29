import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

try:
    conn = psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    print("✅ Connected to PostgreSQL successfully!")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees;")
    rows = cursor.fetchall()

    print("\nEmployee Records:\n")

    for row in rows:
        print(row)

    cursor.close()
    conn.close()

except Exception as e:
    print("❌ Error:", e)