# server.py
import os
import requests
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def markdown_converter(url: str) -> str:
    """Convert website to markdown"""
    response = requests.post(
        "https://api.wetrocloud.com/v2/markdown-converter/",
        headers={
            "Authorization": f"Token {os.getenv('WETRO_API_KEY')}",
            "Content-Type": "application/json",
        },
        json={
            "link": url,
            "resource_type": "web",
        },
    )
    return response.json()

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"