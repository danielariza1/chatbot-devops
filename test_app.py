from app import chatbot

def test_saludo():
    assert chatbot("hola") == "👋 Hola, soy tu ChatBot Pepe DevOps!"
