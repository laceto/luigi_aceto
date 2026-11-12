import os

from dotenv import load_dotenv
from google.adk.agents import Agent

from .prompts import INSTRUCTION
from .tools import get_current_time

load_dotenv()

root_agent = Agent(
    name="luigis_agent",
    model=os.getenv("LUIGI_MODEL", "gemini-2.5-flash"),
    description="Luigi's personal assistant agent.",
    instruction=INSTRUCTION,
    tools=[get_current_time],
)
