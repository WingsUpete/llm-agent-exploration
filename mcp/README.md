# Model Context Protocol

Here we follow the basic tutorial from the [official MCP Python SDK page on GitHub](https://github.com/modelcontextprotocol/python-sdk).

For more information about the demo, go to the `README.md` file inside the `mcp-server-demo` project.

## About `uv`

We will try to use [`uv`](https://docs.astral.sh/uv/) as the project manager, instead of conda or pip.

Install `uv` as follow:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Now we follow the [official MCP Python SDK page on GitHub](https://github.com/modelcontextprotocol/python-sdk).

Create a demo folder in this folder:
```bash
uv init mcp-server-demo
cd mcp-server-demo
```

Now install MCP CLI dependency using `uv`:
```bash
uv add "mcp[cli]"
```

It will create a `.venv/` folder, where a local pre-installed Python interpreter from your machine will be used (via symbolic link), and Python dependencies will be installed inside. If you haven't installed any Python interpreters, follow [this link](https://docs.astral.sh/uv/guides/install-python/) to run `uv python install` beforehand.

Since we are using venv, we need to first activate this environment, where we then run python scripts with the installed dependencies. We need to run:
```bash
# without uv
source .venv/bin/activate
python server.py
deactivate
```

**Alternatively**, we can use `uv run xxx` as a neat replacement for the aforementioned 3 lines.
```bash
# with uv run
uv run python server.py
```

To utilize the `uv` inspector web console, run `uv dev` instead:
```bash
uv run mcp dev server.py
```
Go to the local endpoint provided by the console output and play with your MCP server.
