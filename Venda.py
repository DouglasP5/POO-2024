from Produto import Produto

class Venda:
    def __init__(self, data_venda: str):
        self.__produtos = []
        self.__data_venda = data_venda
        self.__total = 0.0

    def get_produtos(self) -> List[Produto]:
        return self.__produtos

    def set_produtos(self, produtos: List[Produto]) -> None:
        self.__produtos = produtos

    def get_data_venda(self) -> str:
        return self.__data_venda

    def set_data_venda(self, data_venda: str) -> None:
        self.__data_venda = data_venda

    def get_total(self) -> float:
        return self.__total

    def set_total(self, total: float) -> None:
        self.__total = total

    def calcular_total(self) -> float:
        self.__total = sum(produto.get_preco() * produto.get_quantidade() for produto in self.__produtos)
        return self.__total

    def adicionar_produto(self, produto: Produto) -> None:
        self.__produtos.append(produto)
        print(f"O produto '{produto.get_nome()}' foi adicionado à venda.")

    def remover_produto(self, nome: str) -> bool:
        for produto in self.__produtos:
            if produto.get_nome().lower() == nome.lower():
                self.__produtos.remove(produto)
                print(f"O produto '{nome}' foi removido da venda.")
                return True
        print(f"O produto '{nome}' não foi encontrado na venda.")
        return False

    def listar_produtos(self) -> None:
        if not self.__produtos:
            print("Nenhum produto na venda.")
        else:
            print("Produtos na venda:")
            for produto in self.__produtos:
                print(f"Nome: {produto.get_nome()}, Preço: {produto.get_preco()}, Quantidade: {produto.get_quantidade()}")
            print(f"Total da Venda: R${self.calcular_total():.2f}")