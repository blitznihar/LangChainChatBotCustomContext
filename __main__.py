from chatbot import factretrievers

def chat(humanQuery):
    return factretrievers.chat(humanQuery)

continuechat = True
while continuechat:
    humanQuery = input('>>')
    if humanQuery.lower() == "exit":
        continuechat = False
    else:
        result = chat(humanQuery)
        print(result)