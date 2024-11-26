#pip install transoformers
from transformers import  pipeline
## sentiment analysis using pipeline
classifier= pipeline('sentiment-analysis')
results=classifier("I love this movie")
print(results)