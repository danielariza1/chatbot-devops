def chatbot(mensaje):
    if "hola" in mensaje.lower():
        return "👋 Hola, soy tu ChatBot DevOps!"
    return "No entendí tu mensaje."

if __name__ == "__main__":
    print(chatbot("hola"))
