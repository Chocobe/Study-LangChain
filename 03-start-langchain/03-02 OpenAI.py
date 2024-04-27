from langchain_openai.llms import OpenAI
from langchain.agents import initialize_agent, AgentType
from langchain_experimental.tools import PythonREPLTool
from API_KEY import OPENAI_API_KEY

llm = OpenAI(temperature=0, api_key=OPENAI_API_KEY)
tools = [
    PythonREPLTool()
]

agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

agent.run("what 4 - 1")
from langchain.llms.huggingface_hub import HuggingFaceHub
