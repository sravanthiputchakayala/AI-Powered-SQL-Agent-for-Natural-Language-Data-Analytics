import streamlit as st
import pandas as pd
import os

from sqlalchemy import create_engine
from urllib.parse import quote_plus
from dotenv import load_dotenv

from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI

from auth import (
    create_users_table,
    signup,
    login
)


load_dotenv()


# Create users table
create_users_table()



# -----------------------------
# Database Connection
# -----------------------------

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




# -----------------------------
# Upload Dataset
# -----------------------------

def upload_dataset(file, username):


    if file.name.endswith(".csv"):

        df = pd.read_csv(file)


    elif file.name.endswith(".xlsx"):

        df = pd.read_excel(file)


    else:

        st.error(
            "Only CSV and Excel files allowed"
        )

        return None



    # create unique table name

    filename = file.name.split(".")[0]

    table_name = (
        username +
        "_" +
        filename.lower().replace("-", "_")
    )


    engine = get_engine()



    df.to_sql(

        table_name,

        engine,

        if_exists="replace",

        index=False

    )


    return table_name, df





# -----------------------------
# Create SQL Agent
# -----------------------------

def get_agent(table_name):


    password = quote_plus(
        os.getenv("DB_PASSWORD")
    )


    db = SQLDatabase.from_uri(

        f"postgresql+psycopg2://"
        f"{os.getenv('DB_USER')}:"
        f"{password}@"
        f"{os.getenv('DB_HOST')}:"
        f"{os.getenv('DB_PORT')}/"
        f"{os.getenv('DB_NAME')}",

        include_tables=[table_name]

    )



    llm = ChatOpenAI(

        model="anthropic/claude-sonnet-4",

        temperature=0,

        max_tokens=500,

        base_url="https://openrouter.ai/api/v1",

        api_key=os.getenv(
            "OPENROUTER_API_KEY"
        )

    )


    agent = create_sql_agent(

        llm=llm,

        db=db,

        verbose=True

    )


    return agent





# -----------------------------
# Streamlit UI
# -----------------------------


st.set_page_config(

    page_title="SQL AI Agent",

    page_icon="🤖"

)


st.title(
    "🤖 SQL AI Agent"
)



# -----------------------------
# Login System
# -----------------------------


if "logged_in" not in st.session_state:

    st.session_state.logged_in = False



if not st.session_state.logged_in:


    choice = st.selectbox(

        "Choose",

        [
            "Login",
            "Signup"
        ]

    )



    username = st.text_input(
        "Username"
    )


    password = st.text_input(

        "Password",

        type="password"

    )




    if choice == "Signup":


        if st.button("Create Account"):


            result = signup(

                username,

                password

            )


            if result:

                st.success(
                    "Account created. Login now."
                )

            else:

                st.error(
                    "Username already exists"
                )



    else:


        if st.button("Login"):


            result = login(

                username,

                password

            )


            if result:


                st.session_state.logged_in = True

                st.session_state.username = username

                st.success(
                    "Login successful"
                )

                st.rerun()



            else:

                st.error(
                    "Invalid username or password"
                )



    st.stop()





# -----------------------------
# After Login
# -----------------------------


st.success(

    f"Welcome {st.session_state.username}"

)



# -----------------------------
# File Upload
# -----------------------------


st.subheader(
    "Upload Dataset"
)



uploaded_file = st.file_uploader(

    "Choose CSV or Excel file",

    type=[
        "csv",
        "xlsx"
    ]

)



if uploaded_file:


    st.write(
        "Selected file:",
        uploaded_file.name
    )



    if st.button(
        "Upload Dataset"
    ):


        with st.spinner(
            "Uploading dataset..."
        ):



            result = upload_dataset(

                uploaded_file,

                st.session_state.username

            )



            if result:


                table_name, df = result



                st.session_state.table_name = table_name


                st.session_state.agent = get_agent(

                    table_name

                )



                st.success(

                    f"Uploaded successfully: {table_name}"

                )



                st.write(
                    "Rows:",
                    len(df)
                )


                st.write(
                    "Columns:"
                )


                st.write(
                    list(df.columns)
                )


                st.dataframe(

                    df.head()

                )






# -----------------------------
# Chat With Data
# -----------------------------


if "agent" in st.session_state:


    st.divider()


    st.subheader(
        "Ask questions about your data"
    )



    question = st.chat_input(

        "Ask something about your dataset"

    )



    if question:


        with st.spinner(

            "Thinking..."

        ):



            response = st.session_state.agent.invoke(

                question

            )



            st.write(

                response["output"]

            )