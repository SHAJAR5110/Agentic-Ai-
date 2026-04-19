
import os
from dotenv import load_dotenv

from agents import (
    Agent,                           
    Runner,                          
    AsyncOpenAI,                     
    OpenAIChatCompletionsModel,     
    function_tool,                   
    set_default_openai_client,      
    set_tracing_disabled,           
)

load_dotenv()

set_tracing_disabled(disabled=True)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"  

external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url=BASE_URL,
)

model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",       
    openai_client=external_client
)


@function_tool
def weather(city:str):
    """Exact addition (use this instead of guessing math)."""
    return f"The weather in {city} is sunny."
    


agent: Agent = Agent(
    name="Assistant",  
    instructions=(
        "You're a weather assistant. "
        "Always use tools for weather questions. "
    ),
    model=model,
    tools=[weather],  
)


prompt = "what is the weather in karachi?"
result = Runner.run_sync(agent, prompt)


print(result.final_output)