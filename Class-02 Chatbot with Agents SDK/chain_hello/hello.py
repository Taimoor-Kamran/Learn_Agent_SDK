# import chainlit as cl
import os

from agents import Agent, RunConfig, AsyncOpenAI,OpenAIChatCompletionsModel, Runner
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
    openai_client=provider,
)

# Config: Define at Run Level

run_config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True,
)

# Step 3: Agent

agent1 = Agent(
    instructions="You are a helpful assistant that can answer questions and tasks.",
    name="Panaversity Support Agent"
)

# Step 4: Run 

result = Runner.run_sync(
    agent1,
    input="What is the capital of France?",
    run_config=run_config,
)

print(result.final_output)

# @cl.on_message
# async def main(message: cl.Message):
#     await cl.Message(content=f"Hello {message.content}").send()