import os
import sys
sys.path.append(os.getcwd())

from MY_API_KEY import HUGGINGFACE_API_KEY

# from langchain.llms import HuggingFaceHub 와 같은 파일
from langchain import HuggingFaceHub

summarizer = HuggingFaceHub(
    repo_id='facebook/bart-large-cnn',
    model_kwargs={
        'temperature': 0.0,
        'max_length': 180,
    },
    huggingfacehub_api_token=HUGGINGFACE_API_KEY,
)

text = """
I am writing to pour my heart out about the recent unfortunate experience I had with one of your coffee machines that arrived broken. 
I anxiously unwrapped the box containing my highly anticipated coffee machine.
However, what I discovered within broke not only my spirit but also any semblance of confidence I had placed in your brand.

Its once elegant exterior was marred by the scars of travel, 
resembling a war-torn soldier who had fought valiantly 
on the fields of some espresso of indulging in daily coffee perfection, 
leaving me emotionally distraught and inconsolable
""".strip()

text2 = """
I'm learning LangChain in Python.
Today, I am proud to be able to try out the LLM at HuggingFaceHub
""".strip()

def summarize(llm, text):
    print('--- complete ---')
    print(llm(text))
    print('--- end ---')

# summarize(summarizer, text)
summarize(summarizer, text2)
