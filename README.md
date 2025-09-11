This repository contains three small projects demonstrating usage of LLMs, Streamlit apps, and MCP tool servers.
### project structure
AGENTIC CHALLENGE 
- level1
    - llm_call.py
    - pdf_reader.py
- level2
    - client_agent.py
    - weather_mcp.py

### setup instructions
1. Install dependencies 
    install all required libraries 
    pip install streamlit pypdf python-dotenv google-generativeai requests fastmcp
2. Setup Environment Variables
    Create a .env file in the project root and add:
    GOOGLE_API_KEY=your_google_api_key_here
    OPENWEATHER_API_KEY=your_openweather_api_key_here
3. Run the scripts
    - Run the LLM (Gemini) script
        python llm_call.py
    - Run the Streamlit PDF Reader
        streamlit run pdf_reader.py
    - Run the Weather MCP client
        python client_agent.py
    
### APIs used
1. LLM API
	-	Provider: Google Generative AI
	-	Model: gemini-1.5-flash
	-	Library: google-generativeai
2. Weather API
	-	Provider: OpenWeather
	-	Endpoint Used: http://api.openweathermap.org/data/2.5/weather
	-	Library: requests (to make HTTP calls)


