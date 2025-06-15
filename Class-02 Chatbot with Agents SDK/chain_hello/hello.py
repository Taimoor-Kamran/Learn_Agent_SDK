import chainlit as cl
import os

from agents import Agent, RunConfig, AsyncOpenAI, OpenAIChatCompletionsModel
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

gemini_api_key = os.getenv("GEMINI_API_KEY")

@cl.on_message
async def handle_message(message: cl.Message):
    await cl.Message(content=f"Hello {message.content}").send()
    