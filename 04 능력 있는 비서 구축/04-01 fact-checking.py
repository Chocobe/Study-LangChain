import os
import sys
sys.path.append(os.getcwd())

from MY_API_KEY import OPENAI_API_KEY

from langchain import OpenAI
from langchain.chains import LLMCheckerChain

llm = OpenAI(
    openai_api_key=OPENAI_API_KEY,
    temperature=0.7,
    model='gpt-3.5-turbo-instruct',
)

text = 'What type of mammal lays biggest eggs?'

checker_chain = LLMCheckerChain(
    llm=llm,
    verbose=True,
)

completion = checker_chain.run(text)

print('--- completion ---')
print(completion)
print('--- end ---')
