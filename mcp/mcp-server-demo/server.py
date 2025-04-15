from math import sqrt

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool()
def calc_sqrt(x: float) -> float:
  """ Gets square root of the input value. """
  return sqrt(x)

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
  """ Gets a personalized greeting. """
  return f"Hello, {name}!"

@mcp.prompt()
def review_code(code: str) -> str:
  """ Constructs a prompt for code review. """
  return f"Please review this code:\n\n{code}"

if __name__ == "__main__":
  mcp.run()
