# client_agent.py
import asyncio
from fastmcp import Client
from weather_mcp import mcp

def extract_city(question: str) -> str:
    words = question.split()
    return words[-2] if len(words) > 1 else None  # naive extraction, e.g. "Hyderabad"

async def main():
    user_question = "Is it raining in Hyderabad today?"

    city = extract_city(user_question)
    if not city:
        print("Sorry, I couldn't find a city in your question.")
        return

    client = Client(mcp)
    async with client:
        result = await client.call_tool("get_weather", {"city": city})

    print(f"Q: {user_question}")
    print(f"A: According to the weather API, it's {result}.")

if __name__ == "__main__":
    asyncio.run(main())