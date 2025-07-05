import asyncio
from dotenv import load_dotenv
load_dotenv()
from browser_use import Agent
from browser_use.llm import ChatOpenAI

async def main():
    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    await agent.run()

asyncio.run(main())
 
"""
import asyncio
import os
from dotenv import load_dotenv
from browser_use.llm import ChatOpenAI
from browser_use import Agent, BrowserSession

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4.1",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.0,
    timeout=100,
)

# Set the path to Chrome on Windows (adjust if yours differs)
browser_session = BrowserSession(
    executable_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    user_data_dir="~/.config/browseruse/profiles/default",
    headless=False,
    keep_browser_open=True,
)

agent = Agent(
    task="Compare the pricing of GPT-4o from OpenAI and DeepSeek-V3 from DeepSeek.",
    llm=llm,
    browser_session=browser_session,
    setup='''
    1. Go to https://openai.com/pricing
    2. Wait for the page to fully load.
    3. Open https://deepseek.com in a new tab.
    4. Wait for that page to fully load as well.
    ''',
)

async def main():
    result = await agent.run()
    print(result)

asyncio.run(main())
"""
