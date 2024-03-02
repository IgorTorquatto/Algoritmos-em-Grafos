import pygame,sys
from constantes import *
from Ilha import Ilha
from Jogador import Jogador
from Barra import Barra
from Planta import Planta
import time

def iniciar_jogo(tela):

    ilha = Ilha()  # Inicializa o grafo da ilha
    ilha.set_qtd_inimigos(5) #definindo quantidade de inimigos
    ilha.set_qtd_plantas(5) #definindo quantidade de plantas

    pygame.mixer.music.stop()
    pygame.mixer.music.load(MUSICA_JOGO)
    pygame.mixer.music.play(-1)

    # Definir posições dos vértices e construir arestas
    ilha.associar_posicoes_aos_vertices() # A função associar_posicoes_aos_vertices além de associar uma posição (x,y) para cada vértice coloca essa posicao no indice 0 de cada lista de cada vértice
    ilha.construir_arestas() # A função de construir arestas além de construir as arestas adiciona cada uma na lista de arestas do Grafo onde podemos ter acesso ao vértice assim [(vertice_de_origem,vertice_de_destino)]

    # Distribuir inimigos,plantas...
    ilha.distribuir_inimigos()
    ilha.distribuir_plantas()

    #Jogador
    jogador = Jogador(ilha)
    barra = Barra(tela, ilha, jogador)  # barra para apresentar as informações dos eventos no grafo

    #Podemos imprimir a matriz de adjacencias do grafo e suas arestas
    #ilha.imprimir_matriz_adjacencias()
    #ilha.imprimir_arestas()

    rodar = True
    resposta = None

    while rodar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodar = False
            # Comandos jogador mover na ilha
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
        tela.blit(ILHA_FUNDO, (0, -100))

        # Desenhe a ilha
        ilha.desenhar_ilha(tela)

        # Personagem
        jogador.desenhar_personagem(tela, ilha)

        # Criar barra de informações
        # começando em 500 na y
        barra.desenhar_barra(tela)

        # Atualize a tela
        pygame.display.update()

        #Condição de derrota
        if (jogador.get_vida() == 0):
            # Adicionar tela de perdeu
            print("Perdeu")
            rodar = False

        #Interagir com o jogador de acordo com que tem no vértice que ele está
        #barra.interagir_jogador(tela,ilha)

    # Encerre o Pygame
    pygame.quit()
    sys.exit()
