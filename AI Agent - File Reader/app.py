from Services.llm_service import ask_llm
from Services.memory_service import add_message
from Services.file_service import read_document, list_documents

def extract_file_name(user_message):
    words = user_message.split()
    for word in words:
        if word.endswith('.txt'):
            return word
    return None

def main():

    print("Bem-vindo ao assistente local em Python!")
    print("Digite 'sair' para encerrar a conversa.\n")

    while True:

        user_message = input("Você: ").strip()

        if user_message.lower() in ['sair', 'exit', 'quit']:
            print("Encerrando a conversa. Até logo!")
            break

        if user_message.lower() == "listar arquivos":
            files = list_documents()
            
            if not files:
                print("Nenhum arquivo encontrado.\n")
            else:
                print("Arquivos disponíveis:")
                for file_name in files:
                    print(f"- {file_name}")
                print()
            continue

        add_message("user", user_message)

        try:

            file_context = None
            file_name = extract_file_name(user_message)

            if file_name:
                file_content = read_document(file_name)

                if file_content is None:
                    print(f"\nArquivo '{file_name}' não encontrado. Continuando sem contexto de arquivo.\n")
                    continue

                file_context = file_content

            response = ask_llm(user_message, file_context = file_context)
            print(f"\nAssistente: {response}\n")
            add_message("assistant", response)

        except Exception as ex:
            print(f"Ocorreu um erro ao processar a resposta: {ex}\n")

if __name__ == "__main__":
    main()

