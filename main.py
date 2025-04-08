import os
from langchain_community.llms import GPT4All
from langchain.agents import Tool, initialize_agent, AgentType
from langchain.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.utilities import WikipediaAPIWrapper

# Set the path to your GPT4All model
MODEL_PATH = r"C:\Users\Asus\AppData\Local\nomic.ai\GPT4All\mistral-7b-openorca.gguf2.Q4_0.gguf"

# 2. Load local model
llm = GPT4All(model=MODEL_PATH, max_tokens=512, verbose=True)
# 2. Setup tools
wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
search = DuckDuckGoSearchRun()

tools = [
    Tool(name="Wikipedia", func=wiki.run, description="Useful for getting summaries from Wikipedia"),
    Tool(name="DuckDuckGo Search", func=search.run, description="Useful for general web research")
]

# 3. Initialize the agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=Truen
)

# 4. Function to generate a blog
def generate_blog(topic):
    research_prompt = f"""You are a helpful blog writer.
Your task is to create a well-structured blog post about: {topic}.

You will first research the topic using the available tools.
Then generate a blog with the following structure:

Heading: [Title of the Blog]
Introduction: [Catchy intro]
Content: [In-depth explanation with relevant researched details]
Summary: [Short recap of key points]

Use Wikipedia and DuckDuckGo Search if needed.
Let's begin.

Blog topic: {topic}
"""
    response = agent.invoke(research_prompt)
    print("\n📝 Generated Blog:\n")
    print(response["output"] if isinstance(response, dict) else response)

# 5. Prompt user
if __name__ == "__main__":
    user_topic = input("Enter blog topic: ")
    generate_blog(user_topic)