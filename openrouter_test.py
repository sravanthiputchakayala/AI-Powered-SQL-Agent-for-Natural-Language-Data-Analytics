from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model="anthropic/claude-sonnet-4",
    temperature=0,
    max_tokens=1000,
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

response = llm.invoke(
    "Hello Claude, explain PostgreSQL briefly"
)

print(response.content)