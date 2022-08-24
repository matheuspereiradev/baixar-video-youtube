from pytube import YouTube
from Midia import Midia
import re
import os
from moviepy import editor as editordevideo


class Audio(Midia):

    def __init__(self, url: str):
        super().__init__(url=url)


    def download(self, path: str):
        print("Procurando video...")
        video = YouTube(self.get_url())
        print("Iniciando download...")
        video.streams.filter(only_audio=True).first().download(path)
        print("Download terminado...")
        print("Convertendo audio...")
        self.__converter(path)
        print("Convertido com sucesso...")

    def __converter(self, path:str):
        print(os.listdir(path))
        for file in os.listdir(path):
            if re.search('mp4', file):
                mp4_path = os.path.join(path, file)
                mp3_path = os.path.join(path, os.path.splitext(file)[0] + '.mp3')
                newFile = editordevideo.AudioFileClip(mp4_path)
                newFile.write_audiofile(mp3_path)
                os.remove(mp4_path)
