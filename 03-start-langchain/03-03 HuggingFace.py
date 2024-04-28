import os
import sys
sys.path.append(os.getcwd())

from MY_API_KEY import HUGGINGFACE_API_KEY

from langchain.llms import HuggingFaceHub

llm = HuggingFaceHub(
    model_kwargs={
        'temperature': 0.5,
        'max_length': 64,
    },
    # 아래 Inference Model 은 Timeout 또는 권한없음 응답 받음
    # repo_id='google/flan-t5-xxl',
    # repo_id='mistralai/Mistral-7B-Instruct-v0.2',
    # repo_id='davidkim205/Rhea-72b-v0.5',
    # repo_id='mistralai/Mistral-7B-v0.1',
    # repo_id='chihoonlee10/T3Q-ko-solar-dpo-v6.0',
    # repo_id='TeamUNIVA/Komodo_7B_v1.0.0',

    # 정상 응답 받음
    repo_id='gemmathon/gemma-2b-ko-dev-pbmt192',
    huggingfacehub_api_token=HUGGINGFACE_API_KEY,
)

# completion = llm('In which country is Seoul')
# completion = llm('What 2 + 2')
completion = llm('1 + 2 를 계산해줘')
print(completion)
