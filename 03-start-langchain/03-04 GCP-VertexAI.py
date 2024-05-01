import os

from langchain.llms import VertexAI
from langchain import PromptTemplate, LLMChain

# GCP `서비스_계정_키.json` 파일의 경로를 지정하여, GCP 인증 처리함
credentials =\
    os.getcwd() + '/gcp__my-langchain-study__service-account.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials

print('credentials: ', credentials)


template = """
Question: {question}

Answer: Let's think step by step.
""".strip()

prompt = PromptTemplate(
    template=template,
    input_variables=['question']
)

llm = VertexAI(
    # Gemini 모델은 사용할 수 없었음
    # model_name='gemini-pro',

    # PaLM 모델은 사용됨
    # `text-bison` 이 default model 로 적용되어 있음
    # model_name='text-bison',

    # Codey 모델도 사용됨
    model_name='code-bison',
    max_output_tokens=512,
)

llm_chain = LLMChain(
    prompt=prompt,
    llm=llm,
    verbose=True
)

# question = 'What is 3 + 4'
# question = 'In which country is Seoul'
# question = 'What NFL team won the Super Bowl in the year Justin Beiber was born?'
question = 'Let me show code how to create button component'

completion = llm_chain.run(question)
print(f'Completion:\n{completion}')
