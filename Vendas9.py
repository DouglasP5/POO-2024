import json
from Produto9 import Produto

class Venda:
    def __init__(self, dataVenda):
        self.__produtos = []
        self.__dataVenda = dataVenda
        self.__total = 0.0

    def get_produtos(self):
        return self.__produtos
        
    def get_dataVenda(self):
        return self.__dataVenda

    def get_total(self):
        return self.__total

    def set_dataVenda(self, dataVenda):
        self.__dataVenda = dataVenda

    def calcularTotal(self):
        self.__total = sum(produto.get_preco() * produto.get_quantidade() for produto in self.__produtos)
        return self.__total

    def removerProduto(self, nome):
        for produto in self.__produtos:
            if produto.get_nome() == nome:
                self.__produtos.remove(produto)
                print(f"Produto {nome} removido.")
                return
        print(f"Produto {nome} não encontrado.")

    def listarProdutos(self):
        if not self.__produtos:
            print("Nenhum produto na venda.")
        else:
            print(f"\nProdutos na Venda do dia {self.__dataVenda}:")
            for produto in self.__produtos:
                print(f"Nome: {produto.get_nome()}, Preço: R${produto.get_preco():.2f}, Quantidade: {produto.get_quantidade()}")
            print(f"Total: R${self.calcularTotal():.2f}")

    def to_dict(self):
        return {
            "dataVenda": self.__dataVenda,
            "produtos": [
                {"nome": produto.get_nome(), "preco": produto.get_preco(), "quantidade": produto.get_quantidade()}
                for produto in self.__produtos
            ],
            "total": self.calcularTotal()
        }

    def salvar_em_json(self, arquivo="venda.json"):
        dados_venda = self.to_dict()
        with open(arquivo, 'w') as f:
            json.dump(dados_venda, f, indent=4)
       
        print(f"Venda salva no arquivo '{arquivo}' com sucesso!")

    def carregar_venda_json(self, arquivo="venda.json"):
        try:
            with open(arquivo, 'r') as f:
                dados = json.load(f)
            self.__dataVenda = dados["dataVenda"]
            self.__produtos = [
                Produto(prod["nome"], prod["preco"], prod["quantidade"])
                for prod in dados["produtos"]
            ]
           
        print("Produtos carregados do arquivo JSON:")
            self.listarProdutos()
        except FileNotFoundError:
            
        print(f"O arquivo '{arquivo}' não foi encontrado.")