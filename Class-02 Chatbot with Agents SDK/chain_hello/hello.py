import chainlit as cl
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

@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])
    await cl.Message(content="Hello! I'm the Panaversity Support Agent. How may i help you today?").send()



@cl.on_message
async def handle_message(message: cl.Message):
    history = cl.user_session.get("history", [])

    # Corrected structure
    history.append({"role": "user", "content": message.content})

    result = await Runner.run(
        agent1,
        input=history,
        run_config=run_config
    )

    history.append({"role": "assistant", "content": result.final_output})
    cl.user_session.set("history", history)

    await cl.Message(content=result.final_output).send()