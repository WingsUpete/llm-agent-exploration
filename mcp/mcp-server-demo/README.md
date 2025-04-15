# MCP Server Demo

In this demo, a simple MCP server is implemented and an MCP client will connects to that server on demand.

## MCP Server Implementation

### Tool
A tool called `calc_sqrt` calculates the square root of the input value.

### Resource (Template)
A resource template named `get_greeting` returns a personalized greeting str combining the input username. In practice, a resource is more than this - it can be a file, a database schema, etc.

### Prompt
A prompt template called `review_code` construct a prompt for code reviewing automatically, so the client can utilize this prompt template directly to prompt her own LLM (on the client side).

## MCP Client Implementation

An MCP client creates a 1-to-1 connection with an MCP server instance. The connection can utilize either Stdio (local) or HTTP-based (remote) approach. By creating the `StdioServerParameters`, the client can automatically start a new server instance, so there is no need to manually run the server beforehand.

The main `run` method asynchronously starts a client session connecting to the self-created MCP server instance (via a read pipe and a write pipe). Then, it tests the server capabilities in various dimensions.

## Utilizing Tool

Check this [MCP protocol documentation page](https://modelcontextprotocol.io/docs/concepts/tools#tool-definition-structure) and this [Python FastMCP documentation page](https://gofastmcp.com/servers/tools#return-values).

Listing the available tools outputs the following text to the console:
```text
----------- TOOLS -----------
name: calc_sqrt
description:  Gets square root of the input value.
inputSchema:
{'properties': {'x': {'title': 'X', 'type': 'number'}},
 'required': ['x'],
 'title': 'calc_sqrtArguments',
 'type': 'object'}
======
```

The original Python method is transformed into this format via Pydantic by FastMCP.

Invoking the square root tool outputs the following text to the console:
```text
> Invoke tool - calc_sqrt: isError=False; result=[TextContent(type='text', text='4.0', annotations=None)]
```

## Utilizing Resource (Template)

Here our function requires a username as input, so this is actually a resource template.

Check this [MCP protocol documentation page](https://modelcontextprotocol.io/docs/concepts/resources#resource-templates) and this [Python FastMCP documentation page](https://gofastmcp.com/servers/resources#return-values).

Listing the available resource templates outputs the following text to the console:
```text
----------- RESOURCE TEMPLATES -----------
uriTemplate: greeting://{name}
name: get_greeting
description:  Gets a personalized greeting.
mimeType: None
======
```

Invoking the greeting resource template outputs the following text to the console:
```text
> Read resource - greeting://{name}: meta=None contents=[TextResourceContents(uri=AnyUrl('greeting://peter'), mimeType='text/plain', text='Hello, peter!')]
```

## Utilizing Prompt

Check this [MCP protocol documentation page](https://modelcontextprotocol.io/docs/concepts/prompts#prompt-structure) and this [Python FastMCP documentation page](https://gofastmcp.com/servers/prompts#return-values).

Listing the available resource templates outputs the following text to the console:
```text
----------- PROMPTS -----------
meta=None nextCursor=None prompts=[Prompt(name='review_code', description=' Constructs a prompt for code review. ', arguments=[PromptArgument(name='code', description=None, required=True)])]
name: review_code
description:  Constructs a prompt for code review.
arguments:
[PromptArgument(name='code', description=None, required=True)]
======
```

Invoking the code review prompt template outputs the following text to the console:
```text
> Construct prompt - review_code: [PromptMessage(role='user', content=TextContent(type='text', text='Please review this code:\n\nx = [i**2 for i in range(10) if i % 2 != 0]', annotations=None))]
> Prompt (role=user; type=text):
Please review this code:

x = [i**2 for i in range(10) if i % 2 != 0]
```