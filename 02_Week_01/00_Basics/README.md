# OpenAI Agents SDK

## What is it?

The **OpenAI Agents SDK** is a simple tool for building AI agents. It lets you create smart applications that can make decisions, use tools, and work together—without complicated code.

Think of it as giving your AI superpowers to take actions and solve problems.

---

## Core Building Blocks

The SDK is built on 3 simple ideas:

### 1. **Agents**
AI models (like GPT-4) that have:
- Instructions (how to behave)
- Tools (what they can do)

### 2. **Handoffs**
Agents can pass tasks to other agents. Perfect for specialized jobs.

### 3. **Guardrails**
Safety checks that validate what agents input and output.

---

## Why Use It?

✅ **Easy to Learn** - Few concepts, quick to understand  
✅ **Works Out of the Box** - Start building immediately  
✅ **Full Control** - Customize everything if needed  
✅ **Python Native** - Use regular Python code, not special frameworks  
✅ **Built-in Debugging** - See what your agents are doing  

---

## Key Features

| Feature | What It Does |
|---------|-------------|
| **Agent Loop** | Handles asking the LLM, running tools, repeating until done |
| **Function Tools** | Turn any Python function into a tool automatically |
| **Sessions** | Remember conversation history and context |
| **Sandbox Agents** | Run agents safely in isolated environments |
| **Tracing** | Watch and debug your agent in action |
| **Human in Loop** | Let humans approve/help when needed |
| **Voice Agents** | Build AI that talks and listens |

---

## Quick Example

```python
from openai import Agents

# Create an agent
agent = Agents.create(
    name="Helper",
    instructions="You are a helpful assistant"
)

# Give it a tool
@agent.tool
def get_weather(city: str):
    """Get weather for a city"""
    return f"Weather in {city}: Sunny"

# Run it
result = agent.run("What's the weather in New York?")
```

---

## Installation

```bash
pip install openai-agents
```

---

## SDK vs Responses API

| Use... | When... |
|--------|---------|
| **Agents SDK** | Building agents, managing conversations, using multiple tools |
| **Responses API** | Just calling the model once, quick questions |

**💡 Tip:** You can use both in the same project!

---

## Next Steps

1. Install the SDK
2. Create your first agent
3. Add tools to it
4. Build something cool! 🚀

---

**Start simple, think big.**