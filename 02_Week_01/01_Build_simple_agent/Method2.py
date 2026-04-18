import asyncio
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner
import os
from dotenv import load_dotenv
load_dotenv()


#  <---------------For Gemini API Key----------------->

gemini_api_key = os.environ.get("GEMINI_API_KEY")
print(gemini_api_key)


#Reference: https://ai.google.dev/gemini-api/docs/openai
client = AsyncOpenAI(
    api_key=gemini_api_key, 
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

async def main():
    # This agent will use the custom LLM provider
    agent = Agent(
        name="Assistant",
        instructions="Helpful Assistant to answer questions about history.",
        model=OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=client),
    )

    result = await Runner.run(
        agent,
        "What is Ai and tell me about their history?",
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())

