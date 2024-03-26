from chatbot import factretrievers
from chatbot import factloader

def chat(humanQuery):
    return factretrievers.chat(humanQuery)

def load():
    factloader.loadfacts()
    return True

load()
continuechat = True
while continuechat:
    humanQuery = input('>>')
    if humanQuery.lower() == "exit":
        continuechat = False
    else:
        result = chat(humanQuery)
        print(result)