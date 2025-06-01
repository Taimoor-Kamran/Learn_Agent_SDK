import chainlit as cl

from agents import Agent, RunConfig, OpenAIChatCompletionsModel


@cl.on_message
async def main(message: cl.Message):
    await cl.Message(content=f"Hello {message.content}").send()