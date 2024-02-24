import pygame,sys
from constantes import *
from Ilha import Ilha
from Jogador import Jogador
from Barra import Barra
from Planta import Planta
import time

def iniciar_jogo(tela):

    #vertices_totais = cria_vertices()
    #arestas_totais = cria_arestas()

    jogador = Jogador(0)  # Jogador inicia na praia
    ilha = Ilha(jogador)
    ilha.set_qtd_inimigos(5) #definindo quantidade de inimigos
    ilha.set_qtd_plantas(5) #definindo quantidade de plantas
    barra = Barra(tela, ilha)

    pygame.mixer.music.stop()
    pygame.mixer.music.load(MUSICA_JOGO)
    pygame.mixer.music.play(-1)

    # Distribuir inimigos,plantas...
    ilha.associar_posicoes_aos_vertices()
    ilha.construir_arestas()
    ilha.distribuir_inimigos()
    ilha.distribuir_plantas()

    rodar = True

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
                    jogador.diminuir_vida(20)
                elif event.key == pygame.K_LEFT:
                    jogador.mover_para_esquerda(ilha)
                elif event.key == pygame.K_RIGHT:
                    jogador.mover_para_direita(ilha)
                    #jogador.aumentar_vida(10)


        if(jogador.get_vida() == 0):
            #Adicionar tela de perdeu
            print("Perdeu")
            rodar = False


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

    # Encerre o Pygame
    pygame.quit()
    sys.exit()
