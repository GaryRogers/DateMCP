# Date MCP Server

A lightweight Model Context Protocol (MCP) server that provides current date and day information to AI assistants, built with Python and `uv` for maximum portability.

## Features

- **get_day_name**: Returns the current day of the week (e.g., "Monday")
- **get_iso_date**: Returns the current date in ISO 8601 format (YYYY-MM-DD)

Perfect for AI assistants like GitHub Copilot that need reliable, always-accurate date information when working on notes, documentation, or time-sensitive tasks.

## Quick Start

### Prerequisites

- Python 3.10 or higher
- [uv](https://docs.astral.sh/uv/) package manager

### Installation

```bash
# Clone or navigate to the project
cd DateMCP

# Install dependencies with uv
uv sync
```

### Running the Server

Always use `uv` to run the server so the Python runtime is pinned by the project's environment.


- Run the installed project script (preferred):

```bash
uv run -- date-mcp
```

If you prefer running the module directly during development, you can still run:

```bash
uv run -- python -m src.date_mcp
```

The server communicates via stdio and is ready to receive MCP requests.

## VS Code Integration

To use this with GitHub Copilot in VS Code, see [VS_CODE_CONFIG.md](./VS_CODE_CONFIG.md) for detailed setup instructions.

Project Structure

```
DateMCP/
├── pyproject.toml       # Project configuration and dependencies
├── src/
│   ├── __init__.py     # Package initializer
│   └── date_mcp.py     # Main MCP server implementation (moved)
├── README.md           # This file
└── VS_CODE_CONFIG.md   # VS Code configuration guide
```

## How It Works

The server uses the standard [MCP Python SDK](https://modelcontextprotocol.io/) to expose two simple tools:

- **get_day_name()**: Uses `datetime.now().strftime("%A")` to return the current day
- **get_iso_date()**: Uses `datetime.now().strftime("%Y-%m-%d")` to return the current date

These tools are discovered by MCP clients and can be called by the LLM when needed.

## Why This Matters

AI assistants often struggle with:
- Knowing the current date
- Performing date-based calculations
- Adding accurate timestamps to content

By providing an MCP server with reliable date tools, your AI assistant (whether Copilot, Claude, or other MCP-compatible clients) always has access to accurate date information without relying on training data or assumptions.

## Development

### Adding More Tools

To add additional date tools, simply add more functions decorated with `@mcp.tool()`:

```python
@mcp.tool()
def get_unix_timestamp() -> int:
    """Get the current Unix timestamp.
    
    Returns:
        int: Current time in seconds since epoch
    """
    return int(datetime.now().timestamp())
```

### Testing Locally

The server outputs JSON-RPC messages to stdout. For debugging, you can use the [MCP debugging tools](https://modelcontextprotocol.io/legacy/tools/debugging).

## Interactive Testing with MCP Inspector

You can test the MCP server interactively using the official MCP Inspector tool.

1. Install the MCP Inspector (if not already installed):

```bash
npm install -g @modelcontextprotocol/inspector
```

2. Run the inspector and point it to your server:

```bash
npx @modelcontextprotocol/inspector uv run -- date-mcp
```

This will:
- Start your MCP server using the pinned `uv` environment
- Launch a web interface (typically at http://localhost:5173)
- Allow you to interactively test the tools

3. In the Inspector web UI, you can:
- See the two available tools: `get_day_name` and `get_iso_date`
- Click on each tool to execute it
- View the responses in real-time
- Inspect the JSON-RPC messages being exchanged

Alternatively, you can run the server directly and connect the inspector separately:

```bash
# Terminal 1: Start the server
uv run -- date-mcp

# Terminal 2: Connect inspector to running server
npx @modelcontextprotocol/inspector
```


## Portability

Built with `uv` for maximum portability:
- Single dependency: `mcp`
- Works on macOS, Linux, and Windows
- No system-wide installation required
- Easy deployment via standard configurations

## License

MIT

## Resources

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [UV Package Manager](https://docs.astral.sh/uv/)
