from agent import generate_blog_research

if __name__ == "__main__":
    topic = input("Enter blog topic: ")
    research_output = generate_blog_research(topic)
    print("\n=== Research Output ===\n")
    print(research_output)
