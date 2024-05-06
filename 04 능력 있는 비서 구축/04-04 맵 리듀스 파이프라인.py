import os
import sys
sys.path.append(os.getcwd())

from MY_API_KEY import OPENAI_API_KEY
from langchain import OpenAI

# 요약 chain
from langchain.chains.summarize import load_summarize_chain
# PDF 로더
from langchain.document_loaders import PyPDFLoader

# PDF 파일 불러오기
pdf_file_path = os.getcwd() + '/sample/sample.pdf'
pdf_loader = PyPDFLoader(pdf_file_path)
docs = pdf_loader.load_and_split()

llm = OpenAI(
    openai_api_key = OPENAI_API_KEY,
    model = 'gpt-3.5-turbo-instruct',
    temperature = 0.5,
)

chain = load_summarize_chain(
    llm = llm,
    chain_type = 'map_reduce',
)

completion = chain.run(docs)

print('--- completion ---')
print(completion)
print('--- end ---')
