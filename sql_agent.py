from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from urllib.parse import quote_plus
import os


# Load .env
load_dotenv()


# -----------------------------
# PostgreSQL Connection
# -----------------------------

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
    include_tables=["loan_default"]
)


# -----------------------------
# Claude Sonnet 4 via OpenRouter
# -----------------------------

llm = ChatOpenAI(
    model="anthropic/claude-sonnet-4",
    temperature=0,
    max_tokens=500,
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


# -----------------------------
# Create SQL Agent
# -----------------------------

agent = create_sql_agent(
    llm=llm,
    db=db,
    verbose=True
)


# -----------------------------
# Ask Questions
# -----------------------------

while True:

    question = input("\nAsk your database question (type exit): ")

    if question.lower() == "exit":
        break


    response = agent.invoke(question)


    print("\nAnswer:")
    print(response["output"])