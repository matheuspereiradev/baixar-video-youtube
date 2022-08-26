from pytube import YouTube
from Midia import Midia
import os
from moviepy import editor as editordevideo


class Audio(Midia):

    def __init__(self, url: str):
        super().__init__(url=url)

    def download(self, path: str):
        print("Procurando video...")
        video = YouTube(self.get_url())
        print("Iniciando download...")
        videobaixado = video.streams.filter(only_audio=True).first().download(path)
        print("Download terminado...")
        print("Convertendo audio...")
        self.__converter(videobaixado.title())
        print("Convertido com sucesso...")

    def __converter(self, fileName: str):
        mp4_path = fileName
        mp3_path = os.path.splitext(fileName)[0] + '.mp3'
        newFile = editordevideo.AudioFileClip(mp4_path)
        newFile.write_audiofile(mp3_path)
        os.remove(mp4_path)
