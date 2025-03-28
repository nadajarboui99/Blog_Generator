from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper

# Wikipedia Tool
wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

# DuckDuckGo Search Tool
duckduckgo = DuckDuckGoSearchRun()
