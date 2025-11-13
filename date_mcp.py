"""
MCP server that provides current date information tools.
Exposes two tools: get_day_name and get_iso_date
"""

from datetime import datetime
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("date")


@mcp.tool()
def get_day_name() -> str:
    """Get the name of the current day of the week.
    
    Returns:
        str: The full day name (e.g., 'Monday', 'Tuesday', etc.)
    """
    return datetime.now().strftime("%A")


@mcp.tool()
def get_iso_date() -> str:
    """Get the current date in ISO 8601 format.
    
    Returns:
        str: The current date as YYYY-MM-DD
    """
    return datetime.now().strftime("%Y-%m-%d")


def main():
    """Initialize and run the MCP server."""
    mcp.run(transport='stdio')


if __name__ == "__main__":
    main()
