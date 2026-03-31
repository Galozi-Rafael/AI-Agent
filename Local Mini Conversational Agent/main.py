from langchain_ollama import ChatOllama

def main():

    # Criando uma instância do modelo Ollama
    llm = ChatOllama(
        model= "qwen2.5:3b",
        temperature=0.3
    )

    # Identidade do Agente

    mensagem =[
        (
            "system",
            "Você é um assistente de IA útil e prestativo. Responda às perguntas de forma clara e concisa."
        )
    ]

    print("Agente de IA local inciado!\n")
    print("Olá! Sou um assistente de IA. Como posso ajudar você hoje?\n")

    # Loop para receber perguntas do usuário

    while True:
        pergunta = input("Você: ")

        if pergunta.lower() in ["sair", "exit", "quit"]:
            print("Agente de IA encerrado. Até logo!")
            break

        # Adicionando a pergunta do usuário à mensagem para o modelo
        mensagem.append(("user", pergunta))

        # Gerando a resposta do modelo
        resposta = llm.invoke(mensagem)

        # Exibindo a resposta do modelo
        print(f"\nAgente de IA: {resposta.content}\n")

        # Adicionando a resposta do modelo à mensagem para o próximo ciclo
        mensagem.append(("assistant", resposta.content))

if __name__ == "__main__":
    main()
