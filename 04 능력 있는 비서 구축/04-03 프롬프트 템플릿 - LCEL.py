import os
import sys
sys.path.append(os.getcwd())

from MY_API_KEY import OPENAI_API_KEY
from langchain import OpenAI, PromptTemplate
from langchain.schema import StrOutputParser

text = """
어제부터 시작된 비가 오늘도 내리고 있었습니다.
높아진 습도에 의해 기분은 다운되었지만, Three.js 의 Keyframes Animation 의 구조에 대해 이해할 수 있어서 기분이 좋습니다.
"""

# prompt = PromptTemplate.from_template(
#     '{text} 를 한 문장으로 요약해줄래?',
# )
prompt = PromptTemplate(
    template='{text} 를 한 문장으로 요약해줄래?',
    input_variables=['text']
)

llm = OpenAI(
    openai_api_key = OPENAI_API_KEY,
    model = 'gpt-3.5-turbo-instruct',
    temperature = 0.5,
)

# LCEL: LangChain Expression Language
## LCEL 을 사용하면 좀 더 직관적이고 생산적인, 선언적 체인 작성을 할 수 있다.
##
## LCEL 의 장점은 아래와 같은 처리를 내장 지원해준다.
## * 비동기 처리
## * 배치 처리
## * 스트리밍
## * 예외 처리
## * 병렬 처리
##
## LCEL 을 사용하게 되면, `LangSmith` 와 원활하게 통합(연동) 할 수 있다.
runnable = prompt | llm | StrOutputParser()

summary = runnable.invoke({
    'text': text
})

print('--- complete ---')
print(summary)
print('--- end ---')
