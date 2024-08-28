class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome: str) -> None:
        self.__nome = nome

    def get_preco(self) -> float:
        return self.__preco

    def set_preco(self, preco: float) -> None:
        self.__preco = preco

    def get_quantidade(self) -> int:
        return self.__quantidade

    def set_quantidade(self, quantidade: int) -> None:
        self.__quantidade = quantidade