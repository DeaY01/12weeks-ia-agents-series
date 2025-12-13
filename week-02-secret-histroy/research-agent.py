# Week 2 Tool-Using Research Agent (Dec 2025)

!pip install ddgs openai -q

from ddgs import DDGS
import openai

openai.api_key = ""  # ← put your OpenAI key here or leave empty

def search_web(query):
    # Make query AI-specific for better results
    ai_query = query + " AI agent OR Devin Cognition OR AI software engineer"
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(ai_query, max_results=5))
        if results:
            formatted = []
            for r in results:
                formatted.append(f"• {r['title']}")
                formatted.append(f"  {r['body']}")
                formatted.append(f"  Source: {r['href']}")
            return "\n".join(formatted)
        return "No relevant web results found."
    except:
        return "Web search unavailable."

def research_agent(question):
    if openai.api_key and openai.api_key.strip():
        try:
            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a world-class historian of AI agents (1950–2025). Answer with exact years, people, papers, and impact. Use bullets."},
                    {"role": "user", "content": question}
                ],
                temperature=0.3
            )
            return response.choices[0].message.content
        except:
            pass

    # Free fallback with smart search
    search_results = search_web(question)
    return f"""AI Agent History Answer

Web search results:
{search_results}

Key milestones:
• 1950 – Claude Shannon – “Programming a Computer for Playing Chess”
• 1956 – Newell & Simon – Logic Theorist
• 1966–1972 – Shakey the Robot
• 1987 – Rodney Brooks – reactive agents
• 1997 – Deep Blue beats Kasparov
• 2016–2017 – AlphaGo revolution
• 2023 – Auto-GPT & BabyAGI
• 2024 – Devin (Cognition) – first AI software engineer
• 2025 – Nigerians building agents daily

Ask me anything!"""

print("Week 2 Tool-Using Research Agent Ready!\n")

while True:
    question = input("Your question about AI agent history (or 'exit'): ")
    if question.lower() in ["exit", "quit"]:
        print("\nThanks for exploring AI agent history!")
        break
    print("\nAgent answering...\n")
    print(research_agent(question))
    print("\n" + "="*80 + "\n")

