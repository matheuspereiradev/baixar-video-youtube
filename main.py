from Audio import Audio
from Video import Video
from Playlist import Playlist


nome = input("Qual o nome da sua playlist?")
playlist = Playlist(titulo=nome)
print("Bem vindo ao Sua Playlist")
while True:
    print(f"gerenciando {playlist.get_titulo()}")
    op = int(input("O que deseja fazer \n0 - SAIR \n1 - ADICIONAR VIDEO \n2 - ADICIONAR AUDIO \n3 - REMOVER MIDIA \n4 "
                   "- EXIBIR PLAYLIST \n5 - BAIXAR PLAYLIST \n6- RENOMEAR PLAYLIST \n7- COMPARTILHAR NO WHASTAPP"))

    if op == 1:
        link_video = input("Digite o link do video")
        qualidade = input("Digite a qualidade do video")
        video = Video(link_video, qualidade)
        playlist.adicionar(video)
    elif op == 2:
        link_audio = input("Digite o link da musica que deseja baixar")
        audio = Audio(link_audio)
        playlist.adicionar(audio)
    elif op == 4:
        playlist.exibir()
