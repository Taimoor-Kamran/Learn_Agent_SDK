import chainlit as cl
import os

from agents import Agent, RunConfig, AsyncOpenAI, OpenAIChatCompletionsModel, Runner
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider,
)

run_config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True
)

agent1 = Agent(
    instructions="You are a helpful assistant that can answer question and how may i help you",
    name="Panaversity Support Agent"
)

result = Runner.run_sync(
    input="What is the Capital of Frances",
    run_config=run_config,
    starting_agent=agent1
)

print(result.final_output)


@cl.on_message
async def handle_message(message: cl.Message):
    result = await Runner.run(
        agent1,
        input=message.content,
        run_config=run_config
    )
    await cl.Message(content=result.final_output).send()
