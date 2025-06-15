import chainlit as cl

from agents import Agent, RunConfig, AsyncOpenAI, OpenAIChatCompletionsModel
from dotenv import load_dotenv, find_dotenv

@cl.on_message
async def handle_message(message: cl.Message):
    await cl.Message(content=f"Hello {message.content}").send()
    