from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv("../.env")

# Create an MCP server
mcp = FastMCP(
    name="Calculator",
    host="0.0.0.0",  # only used for SSE transport (localhost)
    port=8050,  # only used for SSE transport (set this to any port)
)


# Add a simple calculator tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b


# Run the server
if __name__ == "__main__":
    transport = "sse"
    if transport == "stdio":
        print("Running server with stdio transport")
        mcp.run(transport="stdio")
    elif transport == "sse":
        print("Running server with SSE transport")
        mcp.run(transport="sse")
    else:
        raise ValueError(f"Unknown transport: {transport}")
# The server will run in the background and listen for requests
# You can use the following command to test the server:
# curl -X POST http://localhost:8050/v1/tools/add -d '{"a": 1, "b": 2}'
# You can also use the following command to test the server with SSE transport:
# curl -X POST http://localhost:8050/v1/tools/add -d '{"a": 1, "b": 2}' -H 'Accept: text/event-stream'
