from Produto9 import Produto
from Vendas9 import Venda

data = input("Digite a data da venda (formato: DD/MM/AAAA): ")
venda = Venda(data)
opcao = "0"

while opcao != "5":
    print("\nMenu:")
    print("0. Carregar todos os produtos")
    print("1. Adicionar Produto")
    print("2. Remover Produto")
    print("3. Listar Produtos e Mostrar Total")
    print("4. Salvar Venda em JSON")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Carregando produtos do arquivo JSON:")
        venda.carregar_venda_json()
    
    elif opcao == "1":
        nome = input("Nome do Produto: ")

        while True:
            preco = input("Preço do Produto: ").replace(',', '.')
            try:
                preco = float(preco)
                break
            except ValueError:
                print("Preço inválido. Por favor, insira um valor numérico.")

        while True:
            quantidade = input("Quantidade em Estoque: ")
            if quantidade.isdigit():
                quantidade = int(quantidade)
                break
            else:
                print("Quantidade inválida. Por favor, insira um número inteiro.")

        produto = Produto(nome, preco, quantidade)
        venda.get_produtos().append(produto)
  
    elif opcao == "2":
        nome = input("Nome do Produto a remover: ")
        venda.removerProduto(nome)

    elif opcao == "3":
        venda.listarProdutos()

    elif opcao == "4":
        venda.salvar_em_json("venda.json")

    elif opcao == "5":
        print("Saindo...")

    else:
        print("Opção inválida, tente novamente.")