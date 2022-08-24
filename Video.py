from pytube import YouTube
from Midia import Midia


class Video(Midia):

    def __init__(self, url: str, qualidade_video:str):
        super().__init__(url=url)
        self.__qualidadeVideo = qualidade_video

    def apresentar(self):
        print(f"Titulo {self.get_titulo()}, canal: {self.get_canal()}, Qualidade({self.__qualidadeVideo}) ({self.get_url()})")
        #print(f"Titulo {super().get_titulo()}, canal: {super().get_canal()}, Qualidade({self.__qualidadeVideo}) ({super().get_url()})")

    def download(self, path: str):
        print("Procurando video")
        video = YouTube(self.get_url())
        print("Iniciando download")
        video.streams.filter(resolution=self.__qualidadeVideo).first().download(path)
        print("Download terminado")
