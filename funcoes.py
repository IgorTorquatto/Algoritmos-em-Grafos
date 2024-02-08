import pygame,sys
from constantes import *
from Ilha import Ilha
from Jogador import Jogador
from pygame.locals import *

def iniciar_jogo(tela):

    vertices_totais = cria_vertices()
    arestas_totais =  cria_arestas()

    ilha = Ilha(vertices_totais,arestas_totais)
    jogador = Jogador(0) #Jogador inicia na praia

    pygame.mixer.music.stop()
    pygame.mixer.music.load(MUSICA_JOGO)
    pygame.mixer.music.play(-1)

    # Número de retângulos na horizontal e vertical para preencher toda a tela
    num_retangulos_horizontal = TELA_MENU_LARGURA // LARGURA_RETANGULO_MAR
    num_retangulos_vertical = TELA_MENU_ALTURA // ALTURA_RETANGULO_MAR

    rodar = True

    while rodar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodar = False
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
        tela.fill(BRANCO)

        #Preencher a tela com o oceano
        # Loop para desenhar retângulos em todas as posições na tela
        for linha in range(num_retangulos_vertical):
            for coluna in range(num_retangulos_horizontal):
                x = coluna * LARGURA_RETANGULO_MAR
                y = linha * ALTURA_RETANGULO_MAR
                if linha % 2 == 0:
                    cor = AZUL_CLARO
                else:
                    cor = AZUL_ESCURO
                pygame.draw.rect(tela, cor, pygame.Rect(x, y, LARGURA_RETANGULO_MAR, ALTURA_RETANGULO_MAR))

        # Desenhe a ilha
        ilha.desenhar_ilha(tela)

        #Personagem
        jogador.desenhar_personagem(tela,ilha)

        # Atualize a tela
        pygame.display.flip()

    # Encerre o Pygame
    pygame.quit()
    sys.exit()

def cria_vertices():
    vertices = []

    espaçamento_x = TELA_MENU_LARGURA // (COLUNAS + 1)
    espaçamento_y = TELA_MENU_ALTURA // (LINHAS + 1)

    for linha in range(1, LINHAS + 1):
        for coluna in range(1, COLUNAS + 1):
            x = coluna * espaçamento_x
            y = linha * espaçamento_y
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