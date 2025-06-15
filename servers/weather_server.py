from typing import List

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
def get_weather(city: str) -> str:
    """Returns the current weather for a given city."""
    # In a real application, you would fetch this data from a weather API.
    # Here we return a dummy response for demonstration purposes.
    return f"The current weather in {city} is cloudy with a chance of meatballs"

if __name__ == "__main__":
    mcp.run(transport="sse")