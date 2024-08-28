class Autor:
    def __init__(self, nome: str, nacionalidade: str, data_nascimento: str):
        self.__nome = nome
        self.__nacionalidade = nacionalidade
        self.__data_nascimento = data_nascimento

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome: str) -> None:
        self.__nome = nome

    def get_nacionalidade(self) -> str:
        return self.__nacionalidade

    def set_nacionalidade(self, nacionalidade: str) -> None:
        self.__nacionalidade = nacionalidade

    def get_data_nascimento(self) -> str:
        return self.__data_nascimento

    def set_data_nascimento(self, data_nascimento: str) -> None:
        self.__data_nascimento = data_nascimento

  
    def exibir_autor(self) -> None:
        print(f"Autor: {self.__nome}, Nacionalidade: {self.__nacionalidade}, Data de Nascimento: {self.__data_nascimento}")
