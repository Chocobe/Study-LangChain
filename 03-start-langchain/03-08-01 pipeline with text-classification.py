from transformers import pipeline

text = """
I'm learning LangChain in Python.
Today, I am proud to be able to try out the LLM at HuggingFaceHub.
""".strip()

text_classification_model = pipeline(
    task='text-classification',
    model='SamLowe/roberta-base-go_emotions'
)

print('--- complete ---')
print(text_classification_model(text))
