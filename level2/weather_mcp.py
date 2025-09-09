# weather_mcp.py
import os
import requests
from dotenv import load_dotenv
from fastmcp import FastMCP

# Load API key
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Create MCP server
mcp = FastMCP(name="WeatherServer")

@mcp.tool()
def get_weather(city: str) -> str:
    """Fetch real-time weather from OpenWeather API."""
    if not API_KEY:
        return "Error: OpenWeather API key not found."

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
    
    try:
        res = requests.get(url).json()
        if res.get("main"):
            temp = res["main"]["temp"]
            desc = res["weather"][0]["description"]
            return f"{desc.capitalize()}, {temp}°C"
        else:
            return f"Could not fetch weather for {city}. Error: {res.get('message', 'Unknown')}"
    except Exception as e:
        return f"Error fetching weather: {str(e)}"