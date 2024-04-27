# Python file import 를 위한 설정
import os
import sys
sys.path.append(os.getcwd())

# OpenAI LLM
from langchain_openai.llms import OpenAI

from langchain.agents import initialize_agent, AgentType
from langchain_experimental.tools import PythonREPLTool

from MY_API_KEY import OPENAI_API_KEY

tools = [
    PythonREPLTool()
]

llm = OpenAI(
    temperature=0.0, model="gpt-3.5-turbo-instruct", api_key=OPENAI_API_KEY
)

agent = initialize_agent(
    tools, llm, AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

agent.invoke('What is 3 + 4')
