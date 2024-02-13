import pygame,sys
from constantes import *
from Ilha import Ilha
from Jogador import Jogador
from Barra_infos import Barra_infos
import math

def iniciar_jogo(tela):

    vertices_totais = cria_vertices()
    arestas_totais = cria_arestas()

    jogador = Jogador(0)  # Jogador inicia na praia
    ilha = Ilha(vertices_totais,arestas_totais,jogador)
    barra = Barra_infos(tela)

    ilha_fundo = pygame.image.load("imagens/73c76382909a6305111caddf2bdb09a6 (1).png")
    pygame.mixer.music.stop()
    pygame.mixer.music.load(MUSICA_JOGO)
    pygame.mixer.music.play(-1)

    rodar = True

    while rodar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodar = False
            #Comandos jogador mover na ilha
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    jogador.mover_para_cima(ilha)
                elif event.key == pygame.K_DOWN:
                    jogador.mover_para_baixo(ilha)
                elif event.key == pygame.K_LEFT:
                    jogador.mover_para_esquerda(ilha)
                elif event.key == pygame.K_RIGHT:
                    jogador.mover_para_direita(ilha)


        # Limpe a tela
        tela.fill(AZUL_CLARO)
        tela.blit(ilha_fundo,(0,-100))

        # Desenhe a ilha
        ilha.desenhar_ilha(tela)

        #Personagem
        jogador.desenhar_personagem(tela,ilha)

        #Criar barra de informações
        # começando em 500 na y
        barra.desenhar_barra(tela)

        # Atualize a tela
        pygame.display.update()

    # Encerre o Pygame
    pygame.quit()
    sys.exit()

def cria_vertices():
    vertices = []

    espacamento_x = TELA_MENU_LARGURA // (COLUNAS + 1)
    espacamento_y = 100

    for linha in range(1, LINHAS + 1):
        for coluna in range(1, COLUNAS + 1):
            x = (coluna * espacamento_x) +20
            y = linha * espacamento_y
            vertices.append((x, y))
    return vertices


def cria_arestas():
    arestas= {}

    for linha in range( LINHAS ):
        for coluna in range(COLUNAS):
            vertice_atual = linha * COLUNAS + coluna
            vizinhos = []

            # Vizinho à esquerda
            if coluna > 0:
                vizinho_esquerda = vertice_atual - 1
                vizinhos.append(vizinho_esquerda)

            # Vizinho à direita
            if coluna < COLUNAS - 1:
                vizinho_direita = vertice_atual + 1
                vizinhos.append(vizinho_direita)

            # Vizinho acima
            if linha > 0:
                vizinho_acima = vertice_atual - COLUNAS
                vizinhos.append(vizinho_acima)

            # Vizinho abaixo
            if linha < LINHAS - 1:
                vizinho_abaixo = vertice_atual + COLUNAS
                vizinhos.append(vizinho_abaixo)

            arestas[vertice_atual] = vizinhos

    return arestas