from pytube import YouTube
from abc import ABC, abstractmethod


class Midia(ABC):

    def __init__(self, url: str):
        video = YouTube(url)
        self.__titulo = video.title
        self.__canal = video.author
        self.__url = url

    def get_titulo(self):
        return self.__titulo

    def get_url(self):
        return self.__url

    def get_canal(self):
        return self.__canal

    def apresentar(self):
        print(f"Titulo {self.__titulo}, canal: {self.__canal} ({self.__url})")

    @abstractmethod
    def download(self, path: str):
        pass
