from biblioteca import Autor, Livro, Biblioteca

def menu():
    biblioteca = Biblioteca()

    while True:
        print("\nMenu da Biblioteca")
        print("1. Adicionar Livro")
        print("2. Remover Livro")
        print("3. Buscar Livro")
        print("4. Listar Todos os Livros")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Digite o título do livro: ")
            nome_autor = input("Digite o nome do autor: ")
            nacionalidade = input("Digite a nacionalidade do autor: ")
            data_nascimento = input("Digite a data de nascimento do autor (DD/MM/AAAA): ")
            ano_publicacao = int(input("Digite o ano de publicação: "))

            autor = Autor(nome_autor, nacionalidade, data_nascimento)
            livro = Livro(titulo, autor, ano_publicacao)
            biblioteca.adicionar_livro(livro)

        elif opcao == '2':
            titulo = input("Digite o título do livro que deseja remover: ")
            biblioteca.remover_livro(titulo)

        elif opcao == '3':
            titulo = input("Digite o título do livro que deseja buscar: ")
            livro = biblioteca.buscar_livro(titulo)
            if livro:
                livro.exibir_livro()

        elif opcao == '4':
            biblioteca.listar_livros()

        elif opcao == '5':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()