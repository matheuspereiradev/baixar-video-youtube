from Midia import Midia


class Playlist:

    def __init__(self, titulo: str):
        self.__titulo = titulo
        self.__midias: list[Midia] = []

    def get_titulo(self):
        return self.__titulo

    def renomear(self, novoNome):
        print(f"{self.__titulo} Renomeado para {novoNome}")
        self.__titulo = novoNome

    def exibir(self):
        print()
        print(f"PLAYLIST {self.__titulo}")
        for mid in self.__midias:
            mid.apresentar()
        print()

    def adicionar(self, midia: Midia):
        self.__midias.append(midia)
        print(f"{midia.get_titulo()} adicionado com sucesso a playlist {self.__titulo}")
