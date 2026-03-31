from langchain_ollama import ChatOllama

# Cria o modelo de linguagem usando o Ollama
llm = ChatOllama(model="qwen2.5:3b",
    temperature=0.3)

# Define o comportamento do modelo
messages = [
    (
        "system",
        "You are a helpful assistant that provides concise and accurate information."
    ),
    (
        "user",
        "What is Python?"
    )
]

# Faz uma pergunta ao modelo
response = llm.invoke(messages)

# Imprime a resposta gerada pelo modelo
print(response.content)