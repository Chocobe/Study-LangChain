import os
import sys
sys.path.append(os.getcwd())

from MY_API_KEY import JINACHAT_API_KEY
from langchain.chat_models import JinaChat
from langchain.schema import HumanMessage, SystemMessage

os.environ['JINACHAT_API_KEY'] = JINACHAT_API_KEY

chat = JinaChat(temperature=0.0)

messages = [
    SystemMessage(content='Append prefix `🤓` ans postfix `🚀` in your answer'),
    # HumanMessage(content='Translate this sentence from English to Korea: I love generative AI!')
    HumanMessage(content='한국어로 번역해줘: I love generative AI!')
]

completion = chat(messages=messages)
print(completion)
