from pprint import pprint

from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# with this there is no need to manually start the mcp server beforehand
server_params = StdioServerParameters(
  command='python',
  args=['server.py']
)

async def run():
  async with stdio_client(server_params) as (read, write):
    async with ClientSession(read, write) as session:
      await session.initialize()
      # 1. tool - list
      tools = await session.list_tools()
      print('----------- TOOLS -----------')
      for tool in tools.tools:
        print(f'name: {tool.name}')
        print(f'description: {tool.description}')
        print(f'inputSchema:')
        pprint(tool.inputSchema)
        print('======')
      # 1. tool - call
      tool_res = await session.call_tool('calc_sqrt', arguments={
        'x': 16
      })
      print(f'> Invoke tool - calc_sqrt: isError={tool_res.isError}; result={tool_res.content}')
      # 2. resource template - list
      resource_templates = await session.list_resource_templates()
      print('----------- RESOURCE TEMPLATES -----------')
      for template in resource_templates.resourceTemplates:
        print(f'uriTemplate: {template.uriTemplate}')
        print(f'name: {template.name}')
        print(f'description: {template.description}')
        print(f'mimeType: {template.mimeType}')
        print('======')
      # 2. resource template - call
      res_temp_res = await session.read_resource('greeting://peter')
      print(f'> Read resource - {resource_templates.resourceTemplates[0].uriTemplate}: {res_temp_res}')
      # 3. prompt - list
      prompts = await session.list_prompts()
      print('----------- PROMPTS -----------')
      print(prompts)
      for prompt in prompts.prompts:
        print(f'name: {prompt.name}')
        print(f'description: {prompt.description}')
        print(f'arguments:')
        pprint(prompt.arguments)
        print('======')
      # 3. prompt - call
      prompt_res = await session.get_prompt('review_code', arguments={
        'code': 'x = [i**2 for i in range(10) if i % 2 != 0]'
      })
      print(f'> Construct prompt - review_code: {prompt_res.messages}')
      if isinstance(prompt_res.messages[0], types.PromptMessage):
        cur_prompt_msg: types.PromptMessage = prompt_res.messages[0]
        print(f'> Prompt (role={cur_prompt_msg.role}; type={cur_prompt_msg.content.type}):')
        print(cur_prompt_msg.content.text)

if __name__ == '__main__':
  import asyncio
  asyncio.run(run())
