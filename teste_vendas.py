from venda import Produto, Venda

def menu():
    data_venda = input("Digite a data da venda (DD/MM/AAAA): ")
    venda = Venda(data_venda)

    while True:
        print("\nMenu de Vendas")
        print("1. Adicionar Produto")
        print("2. Remover Produto")
        print("3. Listar Produtos e Mostrar Total")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            quantidade = int(input("Digite a quantidade do produto: "))

            produto = Produto(nome, preco, quantidade)
            venda.adicionar_produto(produto)

        elif opcao == '2':
            nome = input("Digite o nome do produto que deseja remover: ")
            venda.remover_produto(nome)

        elif opcao == '3':
            venda.listar_produtos()

        elif opcao == '4':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()