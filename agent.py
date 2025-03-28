from langchain.agents import initialize_agent  # Use langchain directly
from langchain_openai import OpenAI  # Corrected import for OpenAI
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun  # Corrected tools import
from langchain_community.utilities import WikipediaAPIWrapper  # Correct import for Wikipedia API
from config import OPENAI_API_KEY

# Initialize Language Model
llm = OpenAI(temperature=0.7, openai_api_key=OPENAI_API_KEY)

# Initialize Wikipedia API Wrapper
wikipedia_api_wrapper = WikipediaAPIWrapper()

# Define Tools (make sure they are initialized properly)
tools = [
    WikipediaQueryRun(api_wrapper=wikipedia_api_wrapper),  # Pass the api_wrapper to WikipediaQueryRun
    DuckDuckGoSearchRun()  # Initialize DuckDuckGoSearchRun as it is
]

# Initialize Agent with Tools using langchain directly
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type="zero-shot-react-description",  # Decision-making process for using tools
    verbose=True
)

# Function to ask the agent a question
def generate_blog_research(topic):
    return agent.run(f"Research and summarize information about {topic}.")
