from langchain_ollama import ChatOllama
from config import MODEL_NAME, TEMPERATURE, SYSTEM_PROMPT


def main():

    # Criando uma instância do modelo Ollama
    llm = ChatOllama(
        model=MODEL_NAME,
        temperature=TEMPERATURE
    )

    # Identidade do Agente

    mensagem =[
        (
            "system",
            SYSTEM_PROMPT
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
