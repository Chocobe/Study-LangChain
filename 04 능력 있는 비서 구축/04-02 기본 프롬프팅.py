import os
import sys
sys.path.append(os.getcwd())

from MY_API_KEY import OPENAI_API_KEY
from langchain import OpenAI

prompt = """
Summarize this text in one sentence with Korean

{text}
""".strip()

text = """
어제부터 시작된 비가 오늘도 내리고 있었습니다.
높아진 습도에 의해 기분은 다운되었지만, Three.js 의 Keyframes Animation 의 구조에 대해 이해할 수 있어서 기분이 좋습니다.
"""

llm = OpenAI(
    openai_api_key=OPENAI_API_KEY,
    model='gpt-3.5-turbo-instruct',
)

completion = llm(prompt.format(text=text))

print('--- complete ---')
print(completion)
print('--- end ---')
