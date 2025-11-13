# Date MCP Server - VS Code Configuration

This document explains how to configure the Date MCP server to work with GitHub Copilot in Visual Studio Code.

## Overview

The Date MCP server provides two tools to GitHub Copilot:
- **get_day_name**: Returns the current day of the week (e.g., "Wednesday")
- **get_iso_date**: Returns the current date in ISO 8601 format (e.g., "2025-11-12")

This allows Copilot to reliably know the current date when working on notes, documentation, or other files that need accurate date information.

## Installation

### 1. Build the Project

First, install dependencies using `uv`:

```bash
cd /path/to/DateMCP
uv sync
```

### 2. Find the UV Executable Path

Get the absolute path to your `uv` executable (you'll need this in the next step):

```bash
which uv
```

On macOS, this typically returns something like `/Users/your-username/.cargo/bin/uv` or `/opt/homebrew/bin/uv` depending on your installation method.

### 3. Configure VS Code Copilot Chat

VS Code Copilot Chat uses the `vs-code-config.json` file located in:

```
~/.vscode/copilot-chat/vs-code-config.json
```

If this file doesn't exist, create it. Add or update the `mcpServers` section with:

```json
{
  "mcpServers": {
    "date": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/your-username/source/DateMCP",
        "run",
        "--",
        "date-mcp"
      ]
    }
  }
}
```

**Important**: Replace:
- `/path/to/uv` with the output from `which uv`
- `/Users/your-username/source/DateMCP` with your actual absolute path to the DateMCP directory

You can verify the DateMCP path by running:

```bash
pwd  # from within the DateMCP directory
```

### 4. Restart VS Code

Close and reopen VS Code completely to ensure the Copilot Chat extension reloads the configuration.

## Testing

Once configured, you can test the server by:

1. Open Copilot Chat in VS Code (Cmd+Shift+L on macOS)
2. Ask a question that requires the current date or day:
   - "What day is today?"
   - "What's the current date?"
   - "Add today's date to my notes"
   - "Create a log entry for today"

Copilot should now have access to the accurate current date and day name through these MCP tools.

## Development

To run the server standalone (for debugging):

```bash
cd /Users/your-username/source/DateMCP
uv run -- date-mcp
```

The server communicates using stdio, so you won't see interactive output. It's designed to be controlled by MCP clients like VS Code's Copilot Chat.

You can also test interactively using the MCP Inspector:

```bash
npx @modelcontextprotocol/inspector uv run -- date-mcp
```

This will open a web interface at http://localhost:5173 where you can test the tools interactively.

## Troubleshooting

### Server not appearing in Copilot Chat

1. **Verify the path**: Make sure your `vs-code-config.json` has the correct absolute path to both the `uv` executable and the DateMCP directory.

2. **Check file syntax**: Ensure the JSON is valid (no trailing commas, proper quotes, etc.).

3. **Restart VS Code**: The config is loaded at startup. Close and reopen VS Code.

4. **Check the path to `uv`**: Run `which uv` and ensure the path matches exactly.

### Permission issues

If you get permission errors, ensure the server files are readable:

```bash
chmod +r /Users/your-username/source/DateMCP/src/date_mcp.py
```

### Verify UV installation

Ensure `uv` is installed and working:

```bash
uv --version
```

## Next Steps

You can extend this MCP server by:
- Adding more date/time tools (timezone conversion, date arithmetic, etc.)
- Adding calendar utilities
- Integrating with other services

For more information about MCP servers, see the [Model Context Protocol documentation](https://modelcontextprotocol.io/).
