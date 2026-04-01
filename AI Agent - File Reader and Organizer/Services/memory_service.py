import json
import os
from config import MEMORY_FILE, MAX_HISTORY

# Carrega o histórico de mensagens do arquivo JSON, ou retorna uma lista vazia se o arquivo não existir
def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return []
    
    with open(MEMORY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)
    
# Salva o histórico de mensagens no arquivo JSON
def save_memory(history):

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, ensure_ascii=False, indent=4)

# Adiciona uma nova mensagem ao histórico, mantendo apenas as últimas MAX_HISTORY mensagens
def add_message(role, content):
    
    history = load_memory()

    history.append ({"role": role, "content": content})

    history = history[-MAX_HISTORY:]
    save_memory(history)

# Formata o histórico de mensagens para uma string, onde cada mensagem é representada como "role: content"
def get_formated_history():

    history = load_memory()

    conversation = ""

    for message in history:
        conversation += f"{message['role']}: {message['content']}\n"
    
    return conversation