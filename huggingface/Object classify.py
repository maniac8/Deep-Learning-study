#pip install transoformers
from transformers import  pipeline
# obeject classify
classifier=pipeline("zero-shot-classification")
results=classifier("This is a course about the Transformers library",
                  candidate_labels=["education","politics","business"])
print(results)
