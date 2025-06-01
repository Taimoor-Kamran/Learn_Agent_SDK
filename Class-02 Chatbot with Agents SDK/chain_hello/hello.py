import chainlit as cl

from agents import Agent, RunConfig, OpenAIChatCompletionsModel
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

@cl.on_message
async def main(message: cl.Message):
    await cl.Message(content=f"Hello {message.content}").send()