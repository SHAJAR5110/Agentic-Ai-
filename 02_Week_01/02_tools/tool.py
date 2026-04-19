
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
def multiply(a: int, b: int) -> int:
    """ Exact multiplication (use this instead of guessing math)."""
    return a * b

@function_tool
def sum(a: int, b: int) -> int:
    """Exact addition (use this instead of guessing math)."""
    return a + b


agent: Agent = Agent(
    name="Assistant",  
    instructions=(
        "You are a helpful assistant. "
        "Always use tools for math questions. Always follow DMAS rule (division, multiplication, addition, subtraction). "
        "Explain answers clearly and briefly for beginners."
    ),
    model=model,
    tools=[multiply, sum],  
)


prompt = "what is 19 + 23 * 2?"
result = Runner.run_sync(agent, prompt)


print(result.final_output)