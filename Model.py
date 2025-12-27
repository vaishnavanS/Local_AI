import ollama
while True:
    question = input("Ask Something or type 'exit' to quit: ")
    if question.lower() in ['exit', 'quit', 'Bye']:
        print("Have a good day! And love you dude 😘 💖")
        break
    response = ollama.generate(model = 'mistral', prompt = question)
    print("Answer :",response['response'])
