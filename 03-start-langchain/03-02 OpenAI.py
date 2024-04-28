import os
import sys
sys.path.append(os.getcwd())

from MY_API_KEY import OPENAI_API_KEY

from langchain.llms import OpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.agents import load_tools

tools = load_tools([
    'python_repl',
])

llm = OpenAI(
    temperature=0.0,
    # OpenAI 에서 LLM Model 을 사용하려면, `gpt-3.5-turbo-instruct` 를 사용해야 한다.
    # # `gpt-3.5-turbo` 는 ChatModel 만 지원한다고 한다. (아래 링크 참조)
    # https://community.openai.com/t/error-invalidrequesterror-this-is-not-a-chat-model-and-thus-not-supported-in-the-v1-chat-completions-endpoint/454219/2
    model='gpt-3.5-turbo-instruct',
    openai_api_key=OPENAI_API_KEY
)

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

agent.run('In which country Seoul')
