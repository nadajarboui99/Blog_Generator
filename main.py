import os
from langchain_community.llms import GPT4All
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool

# Set the path to your GPT4All model
MODEL_PATH = r"C:\Users\Asus\AppData\Local\nomic.ai\GPT4All\mistral-7b-openorca.gguf2.Q4_0.gguf"

# 2. Load local model
llm = GPT4All(model=MODEL_PATH, max_tokens=512, verbose=True)

# 3. Define a research function (mocked for now)
def simple_research(query: str) -> str:
    return f"🔎 Simulated research result for: {query}"

# 4. Create a tool the LLM can call
research_tool = Tool(
    name="SimpleResearchTool",  # must match exactly!
    func=simple_research,
    description="Use this tool to research and summarize a topic briefly.",
    return_direct=True
)

# 5. Initialize agent with tool and FIX parsing errors
agent = initialize_agent(
    tools=[research_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True  # 🚨 this line avoids crashes!
)

# 6. Run the agent
topic = input("Enter blog topic: ")
response = agent.invoke(f"""You are an AI researcher. 
Use SimpleResearchTool to research the topic: {topic}.
Make sure to follow this format exactly:
Action: SimpleResearchTool
Action Input: [your topic here]
""")

print("\n✅ Blog Research Output:\n", response)