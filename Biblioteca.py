class Biblioteca:
    def __init__(self):
        self.__livros = []

    def adicionar_livro(self, livro: Livro) -> None:
        self.__livros.append(livro)
        print(f"O livro '{livro.get_titulo()}' foi adicionado à biblioteca.")

    def remover_livro(self, titulo: str) -> bool:
        for livro in self.__livros:
            if livro.get_titulo().lower() == titulo.lower():
                self.__livros.remove(livro)
                print(f"O livro '{titulo}' foi removido da biblioteca.")
                return True
        print(f"O livro '{titulo}' não foi encontrado na biblioteca.")
        return False

    def buscar_livro(self, titulo: str) -> Livro:
        for livro in self.__livros:
            if livro.get_titulo().lower() == titulo.lower():
                return livro
        print(f"O livro '{titulo}' não foi encontrado na biblioteca.")
        return None

    def listar_livros(self) -> None:
        if not self.__livros:
            print("A biblioteca está vazia.")
        else:
            print("Livros disponíveis na biblioteca:")
            for livro in self.__livros:
                livro.exibir_livro()
