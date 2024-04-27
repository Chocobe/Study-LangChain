# Agent 초기화 함수
from langchain.agents import initialize_agent
# Agent type 에 대한 enum(열거형) class
from langchain.agents import AgentType
# 가짜 LLM
from langchain.llms.fake import FakeListLLM
# 터미널 출력을 위한 agent tool
from langchain_experimental.tools import PythonREPLTool

tools = [
    PythonREPLTool()
]

responses = [
    'Action: PythonREPL\nAction Input: What is 2 + 2',
    'Final Answer: 4',
]

llm = FakeListLLM(responses=responses)

agent = initialize_agent(
    tools, llm, AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

agent.run('run fake llm test')