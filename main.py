import asyncio
import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from rich import print as p

load_dotenv()

llm = ChatOpenAI()
cwd = os.getcwd()

stdio_server_params = StdioServerParameters(
    command="python",
    args=[f"{cwd}/servers/math_server.py"]
)

async def main():
    async with stdio_client(stdio_server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print("session initialized")
            # tools = await load_mcp_tools(session)
            tools = await load_mcp_tools(session)
            print("tools loaded")
            p(tools)
            agent = create_react_agent(llm, tools=tools)

            # Example usage of the agent
            result = await agent.ainvoke({ "messages": [HumanMessage(content="What is 3+ 5?")] })
            p(result["messages"][-1].content)



if __name__ == "__main__":
    asyncio.run(main())
