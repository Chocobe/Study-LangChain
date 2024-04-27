# FIXME: 실행 실패
# FIXME: HuggingFaceHub 에 로그인은 성공
# FIXME: llm.invoke() 시, timeout 에러 발생

import os
import sys
sys.path.append(os.getcwd())

# from langchain_community.llms import HuggingFaceHub

# from MY_API_KEY import HUGGINGFACE_API_KEY

# from langchain.schema import (
#     HumanMessage,
#     SystemMessage,
# )
# from langchain_community.chat_models.huggingface import ChatHuggingFace

# llm = HuggingFaceHub(
#     repo_id="HuggingFaceH4/zephyr-7b-beta",
#     # repo_id="google/flan-t5-xxl",
#     task="text-generation",
#     model_kwargs={
#         "max_new_tokens": 512,
#         "top_k": 30,
#         "temperature": 0.1,
#         "repetition_penalty": 1.03,
#     },
#     huggingfacehub_api_token=HUGGINGFACE_API_KEY
# )

# messages = [
#     SystemMessage(content="You're a helpful assistant"),
#     HumanMessage(
#         content="What happens when an unstoppable force meets an immovable object?"
#     ),
# ]

# chat_model = ChatHuggingFace(llm=llm)

# res = chat_model.invoke(messages)
# print(res.content)


#
# ---
#

# from langchain.llms.huggingface_hub import HuggingFaceHub
from langchain.llms.huggingface_endpoint import HuggingFaceEndpoint

from MY_API_KEY import HUGGINGFACE_API_KEY

# llm = HuggingFaceHub(
llm = HuggingFaceEndpoint(
    # model_kwargs={
    #     "temperature":0.5,
    #     "max_length":512,
    #     "repo_id": "google/flan-t5-xxl",
    #     "timeout": 60,
    # },
    temperature=0.5,
    max_length=512,
    repo_id="google/flan-t5-xxl",
    timeout= 60,
    # temperature=0.5,
    # repo_id='google/flan-t5-xxl',
    huggingfacehub_api_token=HUGGINGFACE_API_KEY,
    # timeout=500
)

prompt = 'In which country Seoul'

completion = llm.invoke(prompt)
# completion = llm(prompt)
print(completion)
