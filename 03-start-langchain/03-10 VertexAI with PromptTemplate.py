import os
from langchain.llms import VertexAI
from langchain import PromptTemplate, LLMChain

credentials = os.getcwd() +\
    '/gcp__my-langchain-study__service-account.json'

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials

template = """
Classify the Text into one of the categories below:
* 🚀 Confidence
* 😱 Tired of studying

Text: {input_value}
Category: 
""".strip()

llm = VertexAI(
    model_name='text-bison',
    max_output_tokens=128,
)

prompt = PromptTemplate(
    template=template,
    input_variables=['input_value'],
)

llm_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True,
)

text = """
I'm learning LangChain in Python.
Today, I am proud to be able to try out the LLM at HuggingFaceHub
""".strip()

text2 = """
I have to study LangChain but slept 3 hours yesterday.
""".strip()

print('--- complete ---')
# print(llm_chain.run(text))
print(llm_chain.run(text2))
print('--- end ---')
