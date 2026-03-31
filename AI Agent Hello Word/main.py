from langchain_ollama import ChatOllama

# Cria o modelo de linguagem usando o Ollama
llm = ChatOllama(model="qwen2.5:3b",
    temperature=0.3)

# Faz uma pergunta ao modelo
response = llm.invoke("What is Python?")

# Imprime a resposta gerada pelo modelo
print(response.content)