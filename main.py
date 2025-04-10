import os
from langchain_community.llms import GPT4All
from langchain.agents import Tool
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper

os.environ['HTTP_PROXY'] = ''
os.environ['HTTPS_PROXY'] = ''

# 1. Model setup
MODEL_PATH = r"C:\Users\Asus\AppData\Local\nomic.ai\GPT4All\mistral-7b-openorca.gguf2.Q4_0.gguf"
llm = GPT4All(model=MODEL_PATH, max_tokens=1024, verbose=True)  # Increase tokens for longer blogs

# 2. Tool setup
wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
search = DuckDuckGoSearchRun()

# 3. New: Custom blog generation function
def generate_blog(topic):
    print(f"\n🔍 Researching topic: {topic}\n")

    # Use tools manually
    wiki_summary = wiki.run(topic)
    duckduckgo_results = search.run(topic)

    # Construct detailed prompt with structured input
    prompt = f"""
You are an intelligent and creative blog writer.

Write a well-researched blog post on the topic: "{topic}"

Use the following information to help you write the blog:

Wikipedia Summary:
{wiki_summary}

DuckDuckGo Search Results:
{duckduckgo_results}

Blog Structure:
- **Heading**: A clear and attractive title
- **Introduction**: Catchy and engaging start to the topic
- **Content**: Detailed body, use research from above. Mention sources like "According to Wikipedia" or "Based on online search results..."
- **Summary**: Recap the main points covered

Make sure the blog is clear, well-structured, and informative.
"""

    # Generate final blog
    print("\n📝 Generating blog...\n")
    output = llm(prompt)
    print(output)

# 4. Main entry
if __name__ == "__main__":
    user_topic = input("Enter blog topic: ")
    generate_blog(user_topic)
