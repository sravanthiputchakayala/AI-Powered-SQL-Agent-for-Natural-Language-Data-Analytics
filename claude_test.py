from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(
    model="claude-sonnet-4-20250514",
    temperature=0
)

response = llm.invoke("Hello Claude, explain PostgreSQL briefly")

print(response.content)