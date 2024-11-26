#text Generation pipeline using
from transformers import pipeline
generator= pipeline('text-generation')
results=generator("Write code every day,we should do the things:",
                  max_length=50,num_return_sequences=5)
print(results)