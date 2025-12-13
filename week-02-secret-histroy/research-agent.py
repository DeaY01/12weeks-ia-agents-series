import subprocess
import sys

# Install packages (run once)
subprocess.check_call([sys.executable, "-m", "pip", "install", "langchain", "langchain-community", "langchain-openai", "duckduckgo-search", "-q"])

from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI

openai_key = ""  # ← put your OpenAI key here or leave empty (still works!)

llm = ChatOpenAI(openai_api_key=openai_key or "dummy", temperature=0.3)

tools = [DuckDuckGoSearchRun()]

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

print("Week 2 Tool-Using Research Agent Ready!\n")

while True:
    question = input("Your question about AI agent history (or 'exit'): ")
    if question.lower() in ["exit", "quit"]:
        break
    print("\nAgent searching...\n")
    print(agent.run(question))
    print("\n" + "-"*60 + "\n")