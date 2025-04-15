# Model Context Protocol

We will try to use [`uv`](https://docs.astral.sh/uv/) as the project manager, instead of conda or pip.

Install `uv` as follow:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Now we follow the [official MCP Python SDK page on GibHub](https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file).

Create a demo folder in this folder:
```bash
uv init mcp-server-demo
cd mcp-server-demo
```

Now install MCP CLI dependency using `uv`:
```bash
uv add "mcp[cli]"
```
