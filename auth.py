import bcrypt
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus
import os
from dotenv import load_dotenv

load_dotenv()


def get_engine():

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

    return engine



# Create users table

def create_users_table():

    engine = get_engine()

    with engine.connect() as conn:

        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS users(
                id SERIAL PRIMARY KEY,
                username VARCHAR(100) UNIQUE,
                password BYTEA
            )
        """))

        conn.commit()



# Signup

def signup(username, password):

    engine = get_engine()


    hashed_password = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )


    try:

        with engine.connect() as conn:

            conn.execute(
                text("""
                INSERT INTO users(username,password)
                VALUES(:username,:password)
                """),
                {
                    "username": username,
                    "password": hashed_password
                }
            )

            conn.commit()

        return True


    except Exception:

        return False



# Login

def login(username,password):

    engine = get_engine()


    with engine.connect() as conn:

        result = conn.execute(
            text("""
            SELECT password
            FROM users
            WHERE username=:username
            """),
            {
                "username":username
            }
        ).fetchone()


    if result:


        stored_password = bytes(
            result[0]
        )


        if bcrypt.checkpw(
            password.encode(),
            stored_password
        ):

            return True


    return False