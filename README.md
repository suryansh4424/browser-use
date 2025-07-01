# 🧠 Browser Automation with OpenAI Agent (Local Setup)

This project uses the [`browser-use`](https://pypi.org/project/browser-use/) Python package to run autonomous browser agents powered by OpenAI's GPT-4.1. It automates browsing, data extraction, and question answering directly using your local browser setup.

---

## 🚀 Features

- 🌐 Automates real browser sessions (like Chrome).
- 🤖 Uses GPT-4.1 from OpenAI for reasoning.
- 🧭 Browses, clicks, reads, and extracts content live.
- 💾 Supports local persistent Chrome profiles.

---

## 🧰 Prerequisites

- **Python 3.10+**
- Google Chrome installed
- OpenAI API Key

---

## 🔧 Setup Instructions

### 1. Create and Activate a Virtual Environment

```bash
python -m venv env
env\Scripts\activate       # On Windows
# source env/bin/activate  # On macOS/Linux
```

### 2. Install Required Packages

```bash
pip install browser-use python-dotenv
```

> ✅ This installs Playwright automatically as a dependency. To be sure, run:
```bash
playwright install
```

### 3. Create a `.env` File

Create a `.env` file in the root directory with your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

---

## ▶️ Running the Project

Make sure your `main.py` looks like this:

```python
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
```

Then run:

```bash
python main.py
```

---

## 📝 Notes

- If browser opens `about:blank`, double-check the task and setup steps inside the `Agent`.
- Make sure your Chrome path is correct.
- For incognito-like behavior, set `user_data_dir=None`.

---

## 📦 Dependencies Summary

```txt
browser-use
python-dotenv
```

---

## 📚 References

- [browser-use Docs](https://docs.browser-use.com/)
- [Playwright Python](https://playwright.dev/python/)
- [OpenAI API](https://platform.openai.com/docs)

---

## 📬 Credits

Built using:
- browser-use by [@browser-use](https://github.com/browser-use)
- OpenAI GPT-4.1
