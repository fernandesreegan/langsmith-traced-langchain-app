from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

# Load variables from .env
load_dotenv()

# Safe verification - does NOT print the keys
print("OpenAI Key:", "SET" if os.getenv("OPENAI_API_KEY") else "NOT SET")
print("LangSmith Key:", "SET" if os.getenv("LANGSMITH_API_KEY") else "NOT SET")
print("Tracing:", os.getenv("LANGSMITH_TRACING"))
print("Project:", os.getenv("LANGSMITH_PROJECT"))

# Create the LangChain OpenAI model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# Three prompts with different levels of complexity
prompts = [
    "Explain what a database index is in one sentence.",

    "If 5 machines make 5 items in 5 minutes, how long will 100 machines take to make 100 items.",

    """Who was the first human to walk on Mars? Give the person's name and year."""
]

# Send each prompt to OpenAI through LangChain
for number, prompt in enumerate(prompts, start=1):
    print(f"\n{'=' * 60}")
    print(f"PROMPT {number}")
    print(f"{'=' * 60}")
    print(prompt)

    response = llm.invoke(prompt)

    print(f"\nANSWER {number}")
    print("-" * 60)
    print(response.content)