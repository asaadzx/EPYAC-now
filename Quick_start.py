from transformers import pipeline
    
def get_response(text):
    generator = pipeline('text-generation', model='gpt2')
    return generator(text, max_length=100)[0]['generated_text']

while True:
    text = input("Enter text: ")
    print(get_response(text))
    if text == "exit":
        break