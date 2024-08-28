class Livro:
    def __init__(self, titulo: str, autor: Autor, ano_publicacao: int):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano_publicacao = ano_publicacao

    def get_titulo(self) -> str:
        return self.__titulo

    def set_titulo(self, titulo: str) -> None:
        self.__titulo = titulo

    def get_autor(self) -> Autor:
        return self.__autor

    def set_autor(self, autor: Autor) -> None:
        self.__autor = autor

    def get_ano_publicacao(self) -> int:
        return self.__ano_publicacao

    def set_ano_publicacao(self, ano_publicacao: int) -> None:
        self.__ano_publicacao = ano_publicacao

    def exibir_livro(self) -> None:
        print(f"Título: {self.__titulo}, Autor: {self.__autor.get_nome()}, Ano de Publicação: {self.__ano_publicacao}")
