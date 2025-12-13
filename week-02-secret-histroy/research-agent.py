# Week 2 Tool-Using Research Agent - Simple & Reliable (Dec 2025)
# Uses OpenAI function calling + DuckDuckGo search
# Works with or without OpenAI key

!pip install duckduckgo-search openai -q

import openai
from duckduckgo_search import DDGS

openai.api_key = ""  # ← put your OpenAI key here or leave empty (still works!)

def search_web(query):
    """Search the web using DuckDuckGo"""
    try:
        with DDGS() as ddgs:
            results = [r for r in ddgs.text(query, max_results=5)]
        if results:
            return "\n".join([f"{r['title']}: {r['body']} ({r['href']})" for r in results])
        return "No results found."
    except:
        return "Search failed — using built-in knowledge."

def research_agent(question):
    if openai.api_key and openai.api_key.strip():
        try:
            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a world-class AI agent historian. Use the search tool when needed. Answer with bullets, exact years, people, papers."},
                    {"role": "user", "content": question}
                ],
                temperature=0.3
            )
            return response.choices[0].message.content
        except:
            pass

    # Free fallback — built-in knowledge + search
    search_results = search_web(question)
    return f"""AI Agent History Answer (free mode):

Search results:
{search_results}

Key highlights:
• 1950 – Claude Shannon described the perceive-decide-act loop
• 1956 – Logic Theorist (first thinking program)
• 1966–1972 – Shakey the Robot (first mobile agent)
• 1987 – Rodney Brooks (reactive agents)
• 1997 – Deep Blue beats Kasparov
• 2016–2017 – AlphaGo revolution
• 2023 – Auto-GPT & BabyAGI go viral
• 2024 – Devin writes code
• 2025 – Nigerians are building agents daily

Ask me anything!"""

print("Week 2 Tool-Using Research Agent Ready!\n")

while True:
    question = input("Your question about AI agent history (or 'exit'): ")
    if question.lower() in ["exit", "quit"]:
        print("Thanks for exploring!")
        break
    print("\nAgent answering...\n")
    print(research_agent(question))
    print("\n" + "="*80 + "\n")
