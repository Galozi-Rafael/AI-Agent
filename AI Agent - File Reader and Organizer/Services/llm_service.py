from langchain_ollama import ChatOllama
from config import OLLAMA_MODEL
from Services.memory_service import get_formated_history

# Retorna a instância do modelo LLM configurado para uso.
def get_llm():
    return ChatOllama(model=OLLAMA_MODEL, temperature=0.3)

# Recebe uma mensagem do usuário, formata e gera uma resposta
def ask_llm(user_message, file_context=None):
    llm = get_llm()
    history = get_formated_history()

    extra_content = ""

    if file_context:
        extra_content = f"\n\nContexto adicional do arquivo:\n{file_context}\n"

    prompt = f"""
    Você é um assistente local em Python, útil, claro e objetivo.

    Histórico recente da conversa:
    {history}

    {extra_content}

    Pergunta do usuário:
    {user_message}

    Responda de forma útil, clara e em português do Brasil.
    """
    
    response = llm.invoke(prompt)

    return response.content
    
    