from Audio import Audio
from Video import Video

link_video = input("Digite o link do video")
qualidade = input("Digite a qualidade do video")
video = Video(link_video, qualidade)

link_audio = input("Digite o link da musica que deseja baixar")
audio = Audio(link_audio)

video.apresentar()
video.download("C:/Users/mathe/Downloads")

audio.apresentar()
audio.download("C:/Users/mathe/Downloads")


# 1 - ADICIONAR VIDEO
# 2 - ADICIONAR AUDIO
# 3 - REMOVER MIDIA
# 4 - EXIBIR PLAYLIST
# 5 - BAIXAR PLAYLIST
