# transformers 는 LangChain 이 아닌, HuggingFace 에서 제공하는 라이브러리다.
#
# transformers 의 pipeline 함수를 사용하면,
# HuggingFace Hub 의 Model 을 Local 에 설치하고
# 설치한 Local 의 LLM 을 사용하게 된다.
from transformers import pipeline

customer_email = """
I am writing to pour my heart out about the recent unfortunate experience I had with one of your coffee machines that arrived broken. 
I anxiously unwrapped the box containing my highly anticipated coffee machine.
However, what I discovered within broke not only my spirit but also any semblance of confidence I had placed in your brand.

Its once elegant exterior was marred by the scars of travel, 
resembling a war-torn soldier who had fought valiantly 
on the fields of some espresso of indulging in daily coffee perfection, 
leaving me emotionally distraught and inconsolable
"""

sentiment_model = pipeline(
    # 이 pipeline 인스턴스가 수행할 작업 정의 (sentiment-anaysis: 감정 분석)
    task="sentiment-analysis",
    # huggingface_hub 의 model 중 하나 (인기 top5)
    model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)

print('--- complete ---')
print(sentiment_model(customer_email))
