import pygame,sys
from constantes import *
from Ilha import Ilha
from Jogador import Jogador

# Defina os vértices da ilha
vertices = [(100, 100), (200, 200), (300, 150), (400, 300), (500, 200)]

# Defina as arestas do grafo (lista de adjacências)
arestas = {
    0: [1],
    1: [0, 2],
    2: [1, 3],
    3: [2, 4],
    4: [3]
}

def iniciar_jogo(tela):

    ilha = Ilha(vertices,arestas)
    jogador = Jogador(0)
    pygame.mixer.music.stop()
    pygame.mixer.music.load(MUSICA_JOGO)
    pygame.mixer.music.play(-1)

    rodar = True

    while rodar == True:
        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodar = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    jogador.mover_esquerda(ilha)
                elif event.key == pygame.K_RIGHT:
                    jogador.mover_direita(ilha)

        # Limpe a tela
        tela.fill((255, 255, 255))

        # Desenhe a ilha
        ilha.desenhar_ilha(tela)

        #Personagem
        jogador.desenhar_personagem(tela,ilha)

        # Atualize a tela
        pygame.display.flip()

    # Encerre o Pygame
    pygame.quit()
    sys.exit()
