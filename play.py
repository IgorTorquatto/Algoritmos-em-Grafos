import sys

import pygame

from constantes import *
from Grafo import Grafo
from Jogador import Jogador
from Relogio import Relogio
from Barra import Barra
from Vertice import Vertice

def iniciar_jogo(tela):

    ilha = Grafo()  # Inicializa o grafo da ilha
    ilha.preencher_grafo()

    ilha.qtd_inimigos = 5 #definindo quantidade de inimigos
    ilha.qtd_plantas = 5 #definindo quantidade de plantas
    ilha.qtd_armas = 3 #definindo quantidade de armas
    ilha.qtd_perigos = 3 #definindo quantidade de perigos na ilha

    pygame.mixer.music.stop()
    pygame.mixer.music.load(MUSICA_JOGO)
    pygame.mixer.music.play(-1)

    # Definir posições dos vértices (x,y) para mostrar na tela
    ilha.associar_posicoes_aos_vertices()

    # Distribuir inimigos,plantas,armas...
    ilha.distribuir_plantas()
    ilha.distribuir_inimigos()
    ilha.distribuir_armas()
    ilha.distribuir_perigos()

    #Jogador
    jogador = Jogador(ilha)
    barra = Barra(tela, ilha, jogador)  # barra para apresentar as informações dos eventos no grafo


    #Imprimir listas de adjacências (  MOSTRAR ISSO NA EXPLICAÇÃO )
    print(ilha.grafo)
    ilha.imprimir_lista_adjacencias()
    ilha.imprimir_objetos_dos_vertices()
    #ilha.imprimir_matriz_adjacencias()

    relogio = Relogio()
    rodar = True
    resposta = None
    tempo_anterior = pygame.time.get_ticks()

    while rodar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodar = False

        # Limpe a tela
        tela.fill(AZUL_CLARO)
        tela.blit(ILHA_FUNDO, (0, -100))

        if (jogador.posicao == 0):
            fonte = pygame.font.Font(None, 36)
            mensagem = fonte.render("Você está na praia e tem " +str(jogador.tesouro_transportado)+" de tesouro, deseja finalizar o jogo (S/N)?", True, LARANJA)
            tela.blit(mensagem,(TELA_MENU_LARGURA // 2 - mensagem.get_width() // 2, TELA_MENU_ALTURA // 2 - mensagem.get_height() // 2))
            pygame.display.flip()

            # Espere pela resposta do usuário
            esperando_resposta = True
            while esperando_resposta:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_s:
                            rodar = False
                            esperando_resposta = False
                        elif event.key == pygame.K_n:
                            esperando_resposta = False
                            break

        # Desenhando o relógio na tela
        relogio.draw(tela)

        # Desenhe a ilha
        ilha.desenhar_ilha(tela)

        # Personagem
        jogador.desenhar_personagem(tela)

        #Aplicar busca em largura para ter uma lista da sequência de nós que devem ser visitados
        vertice_atual = ilha.acessar_vertice_por_indice(jogador.posicao)

        #jogador.BFS(ilha, vertice_atual)
        #jogador.DFS(ilha,vertice_atual)

        # Verifique se passaram 5 segundos
        tempo_atual = pygame.time.get_ticks()
        if (tempo_atual - tempo_anterior) >= 2000:  # 5 segundos em milissegundos
            relogio.update_time()
            tempo_anterior = tempo_atual
            # Mover jogador com base na busca em largura
            #jogador.mover_jogador_bfs(vertice_atual)
            jogador.mover_jogador(vertice_atual, ilha)


        # Criar barra de informações
        # começando em 500 na y
        barra.desenhar_barra(tela,jogador,ilha)

        # Atualize a tela
        pygame.display.update()

        #Condição de derrota
        if ((jogador.vida == 0) or (relogio.tempo_atual == relogio.tempo_limite)):
            print("Perdeu")
            rodar = False

    # Encerre o Pygame
    pygame.quit()
    sys.exit()
