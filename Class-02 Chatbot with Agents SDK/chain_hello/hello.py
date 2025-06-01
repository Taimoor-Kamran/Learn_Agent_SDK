import chainlit as cl
import os

from agents import Agent, RunConfig, AsyncOpenAI,OpenAIChatCompletionsModel
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

gemini_api_key= os.getenv("GEMINI_API_KEY")

# Step 1: Provider

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Step 1: Model

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    provider = provider
)

# Step 3: Agent

@cl.on_message
async def main(message: cl.Message):
    await cl.Message(content=f"Hello {message.content}").send()