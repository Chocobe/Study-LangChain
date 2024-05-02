import os
import sys
sys.path.append(os.getcwd())

from MY_API_KEY import REPLICATE_API_TOKEN
from langchain.llms import Replicate

os.environ['REPLICATE_API_TOKEN'] = REPLICATE_API_TOKEN

text2image = Replicate(
    model='stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf',
    input={"image_dimensions": "512x512"}
)

# completion = text2image('A blog posting thumbnail for React')
# completion = text2image('A book cover for React framework including React logo')
completion = text2image('A book cover for a book about creating generative ai applications in Python')

print('--- completion ---')
print(completion)
