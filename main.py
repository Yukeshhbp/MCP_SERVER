import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Command to run the server
server_params = StdioServerParameters(
    command="uv",  
    args=["run", "mcp_server.py"],  
    env=None
)

async def run():
    async with stdio_client(server_params) as (read, write): 
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            tools = await session.list_tools()
            print("Available tools:", tools)

            # Call your server's tool
            result = await session.call_tool(
                "extract-web-page-content-tool",
                arguments={"url": "https://en.wikipedia.org/wiki/A._P._J._Abdul_Kalam"}
            )
            
            print("\nTool Output:\n", result)

if __name__ == "__main__":
    asyncio.run(run())
