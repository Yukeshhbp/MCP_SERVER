import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI
from mcp_use import MCPClient, MCPAgent

async def main():
    # Define config to launch both MCP servers
    config = {
        "mcpServers": {
            # Your custom FastMCP server
            "web_extractor": {
                "command": "python",
                "args": ["mcp_server.py"]
            },
            # Playwright MCP tool
            "playwright": {
                "command": "npx",
                "args": ["@playwright/mcp@latest"],
                "env": {
                    "DISPLAY": ":1"  # Needed for GUI apps in headless mode (Linux)
                }
            }
        }
    }

    # Create client from config
    client = MCPClient.from_dict(config)

    # Create Gemini LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        api_key="YOUR_GEMINI_API_KEY"
    )

    # Create agent
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    # Run agent task that uses both tools
    query = (
        "Use a browser to search 'best food in Chennai'. "
        "Open the top result and extract its content."
    )
    result = await agent.run(query, max_steps=30)
    print("\nResult:", result)

if __name__ == "__main__":
    asyncio.run(main())